package main

import (
	"context"
	"github/featurefly/featureflagWrite/pkg/featureflagAdmin"
	"github/featurefly/featureflagWrite/pkg/middleware"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	mainCtx := context.Background()
	mainCtx = middleware.DbConnect(mainCtx)
	mainCtx = middleware.PubsubConnect(mainCtx)

	r.Use(middleware.ContextMiddleware(mainCtx))
	v1 := r.Group("/v1")

	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})

	featureAdmin := v1.Group("collection")
	featureAdmin.POST("/", featureflagAdmin.CreateFeatureflagCollectionApi)

	featureflag := v1.Group("featureflag")
	featureflag.POST("/", featureflagAdmin.CreateFeatureflagApi)
	featureflag.PATCH("/", featureflagAdmin.UpdateFeatureflagApi)
	featureflag.DELETE("/", featureflagAdmin.DeleteHandler)
	env := os.Getenv("env")
	if env != "prod" {
		r.Run("0.0.0.0:8083")
	} else {
		r.Run()
	}
}
