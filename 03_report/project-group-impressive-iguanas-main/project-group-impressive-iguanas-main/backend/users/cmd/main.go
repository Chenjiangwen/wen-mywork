package main

import (
	"net/http"
	"os"

	"github.com/featurefly/users/pkg/login"
	"github.com/featurefly/users/pkg/middleware"
	"github.com/featurefly/users/pkg/register"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.Use(middleware.DbConnect)

	r.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, "")
	})

	v1 := r.Group("/v1")

	userRouter := v1.Group("users")

	userRouter.POST("/login", login.LoginApi)
	userRouter.POST("/register", register.RegisterApi)

	env := os.Getenv("env")
	if env != "prod" {
		r.Run("0.0.0.0:8081")
	} else {
		r.Run()
	}

}
