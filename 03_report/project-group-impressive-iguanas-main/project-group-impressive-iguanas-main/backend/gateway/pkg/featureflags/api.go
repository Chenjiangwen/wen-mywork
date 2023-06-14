package featureflags

import (
	"fmt"
	"net/http"

	"github.com/featurefly/gateway/pkg/consts"
	"github.com/featurefly/gateway/pkg/types"
	"github.com/featurefly/gateway/pkg/utils"
	"github.com/gin-gonic/gin"
)

// FindFeatureFlag For end-users.
// response {name:"FeatureFlagName", status:true}
func FindFeatureFlag(c *gin.Context) {
	id := c.Param("id")
	ctx := c.Request.Context()
	if id == "" {
		c.String(http.StatusBadRequest, "please input parameter feature flag name (key=name)")
		return
	}

	// redisClient, redisErr := getRedis(c)
	// if redisErr != nil {
	// 	fLogW("redis is not ready.")
	// } else {
	// 	resCache, err := redisClient.Get(c, name).Result()
	// 	if err == redis.Nil {
	// 		c.JSON(http.StatusOK, gin.H{
	// 			"feature_flag": resCache,
	// 		})

	// 	} else if err != nil {
	// 		fLogW("redis read error.")
	// 	}
	// 	return
	// }

	response, err := HandleFeatureFlag(id, ctx.Value(utils.FEATUREFLAG_SERVICE).(string), httpRequest)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// Save the response to Redis with an expiration time
	// if redisErr == nil {
	// 	err = redisClient.Set(c, name, response, 5*time.Minute).Err()
	// 	if err != nil {
	// 		fLogW("Error saving data to Redis")
	// 	}
	// }

	c.JSON(http.StatusOK, response)
}

// FindFeatureFlag For users.
// response	 eg: [{id: "ffname:projectname:env", ffname:"aa", isOn:true}, {id: "ffname:projectname:env", ffname:"aa", isOn:true}, ...]

func GetFeatureFlags(c *gin.Context) {
	projectId := c.Param("projectName")
	env := c.Param("env")
	ctx := c.Request.Context()

	if projectId == "" {
		c.String(http.StatusBadRequest, "please input parameter feature flag projectname (key= project name)")
		return
	}
	if env == "" {
		c.String(http.StatusBadRequest, "please input parameter environment (key= environment)")
		return
	}

	// featureflagsId := fmt.Sprintf("%s:%s", projectId, env)
	email := c.Value(consts.USER_JWT_KEY).(*types.UserJwt).Email

	// redisClient, redisErr := getRedis(c)
	// if redisErr != nil {
	// 	fLogW("redis is not ready.")
	// } else {
	// 	resCache, err := redisClient.Get(c, featureflagsId).Result()
	// 	if err == redis.Nil {

	// 	} else if err != nil {
	// 		fLogW("redis read error.")
	// 	}
	// 	c.JSON(http.StatusOK, gin.H{
	// 		"feature_flag": resCache,
	// 	})
	// 	return
	// }
	emailPayload := types.EmailPayload{
		Email: email,
	}

	response, err, code := HandleFeatureFlags(projectId, env, emailPayload, ctx.Value(utils.FEATUREFLAG_SERVICE).(string), utils.CreateHttpPayload, utils.HttpRequest)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// Save the response to Redis with an expiration time
	// if redisErr == nil {
	// 	err = redisClient.Set(c, featureflagsId, response, 5*time.Minute).Err()
	// 	if err != nil {
	// 		fLogW("Error saving data to Redis")
	// 	}
	// }

	c.JSON(code, response)

}

// delete a featureflag
// response http status
func DeleteFeatureFlag(c *gin.Context) {
	ctx := c.Request.Context()

	email := c.Value(consts.USER_JWT_KEY).(*types.UserJwt).Email

	request := DeleteFeatureflagRequestV1{
		Id:    c.Param("id"),
		Email: email,
	}

	if request.Id == "" {
		c.String(http.StatusBadRequest, "please input id")
		c.Abort()
	}

	//TODO: need to get the ff and compare the email in the ff object to see if the user has the permission to delete/update
	ffExist := checkFeatureflagExist(c, request.Id)

	//TODO: http code needs to be changed to 404
	if !ffExist {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "FeatureFlag not found"})
		return
	}

	statusCode, err := handleDeleteFeatureFlag(request, ctx.Value(utils.FEATUREFLAG_WRITE_SERVICE).(string), httpRequest)
	fmt.Print(err)
	if err != nil {
		c.JSON(statusCode, gin.H{"error": "Failed to delete the FeatureFlag"})
		return
	}
	c.JSON(http.StatusOK, gin.H{"message": "FeatureFlag deleted successfully"})
}

func UpdateFeatureFlags(c *gin.Context) {
	ctx := c.Request.Context()
	request := &UpdateFeatureflagRequestV1{}
	if err := c.BindJSON(request); err != nil {
		c.String(http.StatusBadRequest, "the user data model does not match the requirements")
		return
	}

	if request.Env == "" || request.ProjectId == "" || request.FeatureflagName == "" {
		c.String(http.StatusBadRequest, "")
		c.Abort()
	}

	err, code := handleUpdateFeatureFlag(ctx.Value(utils.FEATUREFLAG_WRITE_SERVICE).(string), *request, utils.CreateHttpPayload, utils.HttpRequest)
	if err != nil {
		c.String(code, err.Error())
		return
	}
	c.JSON(code, gin.H{"message": "FeatureFlag updated successfully"})
}

func CreateFeatureflag(c *gin.Context) {
	ctx := c.Request.Context()
	request := &createFeatureflagRequestV1{}
	if err := c.BindJSON(request); err != nil {
		c.String(http.StatusBadRequest, "the user data model does not match the requirements")
		return
	}

	if request.Env == "" || request.ProjectId == "" || request.FeatureflagName == "" {
		c.String(http.StatusBadRequest, "the user data model does not match the requirements")
		return
	}

	// TODO: check if ff exists
	request.Email = c.Value(consts.USER_JWT_KEY).(*types.UserJwt).Email
	err, code := HandleCreateFeatureflag(ctx.Value(utils.FEATUREFLAG_WRITE_SERVICE).(string), *request, utils.CreateHttpPayload, utils.HttpRequest)
	if err != nil {
		c.String(code, err.Error())
		return
	}

	c.JSON(code, "")
}
