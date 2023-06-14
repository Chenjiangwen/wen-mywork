package main

import (
	"github/featurefly/featureflag/pkg/featureflagAdmin"
	"github/featurefly/featureflag/pkg/featureflags"
	"github/featurefly/featureflag/pkg/middleware"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.Use(middleware.DbConnect)
	v1 := r.Group("/v1")

	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})
	//TODO: needs to be changed to featureflag
	featureflagRouter := v1.Group("featureflags")
	featureflagRouter.GET("/:id", featureflags.QueryFeatureflagApi)

	featureAdmin := v1.Group("featureflagAdmin")
	featureAdmin.POST("/featureflag/:projectId/:env", featureflagAdmin.QueryFeatureflagSetApi)

	env := os.Getenv("env")
	if env != "prod" {
		r.Run("0.0.0.0:8082")
	} else {
		r.Run()
	}
}
