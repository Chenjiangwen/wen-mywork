package login

import (
	"net/http"

	"github.com/featurefly/gateway/pkg/types"
	"github.com/featurefly/gateway/pkg/utils"
	"github.com/gin-gonic/gin"
)

func LoginApi(c *gin.Context) {
	ctx := c.Request.Context()
	var user types.UserLoginRequestV1
	err := c.ShouldBind(&user)
	if err != nil {
		c.String(http.StatusBadRequest, "the user data model does not match the requirements")
		return
	}

	ret, err, code := HandleUserLogin(ctx.Value(utils.USER_SERVICE).(string), user, utils.CreateHttpPayload, utils.HttpRequest)
	if err != nil {
		// TODO should set the error code according to the error type
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(code, ret)
}
