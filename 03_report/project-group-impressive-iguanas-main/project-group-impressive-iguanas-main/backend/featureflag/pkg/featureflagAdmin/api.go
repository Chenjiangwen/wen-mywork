package featureflagAdmin

import (
	"encoding/json"
	"github/featurefly/featureflag/pkg/types"
	"net/http"

	"github.com/gin-gonic/gin"
)

func QueryFeatureflagSetApi(c *gin.Context) {
	var payload types.EmailPayload
	err := json.NewDecoder(c.Request.Body).Decode(&payload)

	if err != nil {
		c.String(http.StatusBadRequest, "Failed to decode JSON request")
		return
	}

	request := types.QueryRequestV1{
		ProjectId: c.Param("projectId"),
		Env:       c.Param("env"),
		Email:     payload.Email,
	}

	if request.Env == "" || request.ProjectId == "" {
		c.String(http.StatusBadRequest, "")
		c.Abort()
	}

	response, code, err := queryHandler(getTheCollection(c), request, request.Email, getFeatureflagSet)
	if err != nil {
		c.String(code, err.Error())
		c.Abort()
	}

	c.JSON(code, response)
}
