package middleware

import (
	"context"

	"github.com/gin-gonic/gin"
)

func ContextMiddleware(ctx context.Context) gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Request = c.Request.WithContext(ctx)
		c.Next()
	}
}
