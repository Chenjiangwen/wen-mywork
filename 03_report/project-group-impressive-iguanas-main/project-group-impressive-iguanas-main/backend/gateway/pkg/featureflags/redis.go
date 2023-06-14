package featureflags

import (
	"errors"

	"github.com/gin-gonic/gin"
	"github.com/redis/go-redis/v9"
)

func RedisMiddleware(addr string) gin.HandlerFunc {
	rdb := redis.NewClient(&redis.Options{
		Addr:     addr,
		Password: "",
		DB:       0,
	})

	return func(ctx *gin.Context) {
		ctx.Set("redisClient", rdb)
		ctx.Next()
	}
}

func getRedis(c *gin.Context) (*redis.Client, error) {
	client, exists := c.Get("redisClient")
	if !exists {
		return nil, errors.New("redis client not found in context")
	}
	return client.(*redis.Client), nil
}

//rename file name redis.go
