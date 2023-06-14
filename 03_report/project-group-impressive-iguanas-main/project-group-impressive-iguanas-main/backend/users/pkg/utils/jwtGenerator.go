package utils

import (
	"fmt"
	"time"

	"github.com/featurefly/users/pkg/consts"
	jwt "github.com/golang-jwt/jwt/v5"
)

func GenerateJWT(email string) (string, string, error) {
	var signedToken string
	var tokenType string = consts.TOKEN_TYPE

	// Define the payload for the token
	claims := jwt.MapClaims{
		"email": email,
		"iat":   time.Now().Unix(),
		"iss":   consts.ISS,
		"exp":   time.Now().Add(time.Hour * 1).Unix(),
	}

	// Define the signing method and the signing key
	signingKey := []byte(consts.JWT_KEY)
	signingMethod := jwt.SigningMethodHS256

	// Generate the token with the payload and signing information
	token := jwt.NewWithClaims(signingMethod, claims)
	signedToken, err := token.SignedString(signingKey)
	if err != nil {
		fmt.Println("Error generating token:", err)
		return signedToken, tokenType, err
	}

	return signedToken, tokenType, nil
}
