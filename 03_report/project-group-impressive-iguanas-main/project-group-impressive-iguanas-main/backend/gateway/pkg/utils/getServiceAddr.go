package utils

import (
	"context"
	"os"
)

func GetUserServiceAddr(c context.Context) context.Context {
	env := os.Getenv("env")
	var userService string
	if env != "prod" {
		userService = "http://localhost:8081"
	} else {
		userService = "http://users.default.svc.cluster.local"
	}
	result := context.WithValue(c, USER_SERVICE, userService)
	return result
}

func GetFeatureflagServiceAddr(c context.Context) context.Context {
	env := os.Getenv("env")
	var featureflagService string
	if env != "prod" {
		featureflagService = "http://localhost:8082"
	} else {
		featureflagService = "http://featureflag.default.svc.cluster.local"
	}

	result := context.WithValue(c, FEATUREFLAG_SERVICE, featureflagService)
	return result
}

func GetFeatureflagWriteServiceAddr(c context.Context) context.Context {

	env := os.Getenv("env")
	var featureflagWriteService string
	if env != "prod" {
		featureflagWriteService = "http://localhost:8083"
	} else {
		featureflagWriteService = "http://featureflagwrite.default.svc.cluster.local"
	}

	result := context.WithValue(c, FEATUREFLAG_WRITE_SERVICE, featureflagWriteService)
	return result
}
