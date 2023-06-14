package register

import (
	"fmt"
	"log"
	"net/http"

	"github.com/featurefly/gateway/pkg/collections"
	"github.com/featurefly/gateway/pkg/types"
	"github.com/featurefly/gateway/pkg/utils"
	"github.com/gin-gonic/gin"
)

func RegisterApi(c *gin.Context) {
	ctx := c.Request.Context()
	var user types.UserRegisterRequestV1

	err := c.ShouldBind(&user)
	if err != nil {
		c.String(http.StatusBadRequest, "the user data model does not match the requirements")
		return
	}

	ret, err, code := handleUserRegister(ctx.Value(utils.USER_SERVICE).(string), user, utils.CreateHttpPayload, utils.HttpRequest)
	if err != nil {
		c.String(code, err.Error())
	}

	requests := make([]collections.CreateCollectionRequestV1, 0)
	for _, project := range ret.Projects {
		for _, env := range project.Envs {
			requests = append(requests, collections.CreateCollectionRequestV1{
				Email:     ret.Email,
				ProjectId: project.ID,
				Env:       env,
			})
		}
	}

	for _, request := range requests {
		err, code = collections.HandleCreateCollection(ctx.Value(utils.FEATUREFLAG_WRITE_SERVICE).(string), request, utils.CreateHttpPayload, utils.HttpRequest)
		if err != nil {
			log.Println(http.StatusInternalServerError, fmt.Sprintf("failed to create user collections for user: %s, env: %s, project: %s", request.Email, request.Env, request.ProjectId))
		}
	}

	c.JSON(code, ret)
}
