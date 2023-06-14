package middleware

import (
	"fmt"
	"net/http"

	"github.com/featurefly/users/pkg/consts"
	"github.com/featurefly/users/pkg/types"
	"github.com/gin-gonic/gin"
	jwt "github.com/golang-jwt/jwt/v5"
)

func AuthMiddleware(c *gin.Context) {
	tokenString := c.GetHeader("Authorization")
	claims := &types.UserJwt{}
	if tokenString == "" {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "Authorization header required"})
		c.Abort()
		return
	}

	token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}
		return []byte(consts.JWT_KEY), nil
	})

	if err != nil {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "Invalid authorization token"})
		c.Abort()
		return
	}

	if token.Valid {
		c.Set(consts.USER_JWT_KEY, claims)
		c.Next()
		return
	}

	c.JSON(http.StatusUnauthorized, gin.H{"error": "Invalid authorization token"})
	c.Abort()
	return
}
