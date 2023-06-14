package main

import (
	"os"

	"github.com/featurefly/gateway/pkg/collections"
	"github.com/featurefly/gateway/pkg/featureflags"

	"context"
	"net/http"

	"github.com/featurefly/gateway/pkg/login"
	"github.com/featurefly/gateway/pkg/middleware"
	"github.com/featurefly/gateway/pkg/register"
	"github.com/featurefly/gateway/pkg/utils"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	mainCtx := context.Background()
	mainCtx = utils.GetUserServiceAddr(mainCtx)
	mainCtx = utils.GetFeatureflagServiceAddr(mainCtx)
	mainCtx = utils.GetFeatureflagWriteServiceAddr(mainCtx)
	r.Use(middleware.ContextMiddleware(mainCtx))
	r.Use(middleware.Cors())

	r.GET("/", func(c *gin.Context) {
		c.String(http.StatusOK, "gateway service")
	})

	var redisAddr string
	if os.Getenv("env") != "prod" {
		redisAddr = "localhost:6379"
	} else {
		redisAddr = ""
	}

	v1 := r.Group("/v1")
	userRouter := v1.Group("users")
	userRouter.POST("/login", login.LoginApi)
	userRouter.POST("/register", register.RegisterApi)

	featureflagRouter := v1.Group("featureflags")
	featureflagRouter.Use(featureflags.RedisMiddleware(redisAddr))

	//for enduser to get name: "featureflagname:environment:projectname" and feature
	featureflagRouter.GET("/:id", featureflags.FindFeatureFlag)
	featureflagRouter.POST("/query/:projectName/:env", middleware.AuthMiddleware, featureflags.GetFeatureFlags)
	featureflagRouter.POST("/featureflag", middleware.AuthMiddleware, featureflags.CreateFeatureflag)
	featureflagRouter.DELETE("/:id", middleware.AuthMiddleware, featureflags.DeleteFeatureFlag)
	featureflagRouter.PATCH("/featureflag", middleware.AuthMiddleware, featureflags.UpdateFeatureFlags)

	collection := v1.Group("collection")
	collection.POST("/", middleware.AuthMiddleware, collections.CreateCollection)
	r.Run()

}
