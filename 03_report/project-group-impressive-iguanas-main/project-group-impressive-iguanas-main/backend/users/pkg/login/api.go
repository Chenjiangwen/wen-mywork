package login

import (
	"net/http"

	"github.com/featurefly/users/pkg/db"
	"github.com/featurefly/users/pkg/types"
	"github.com/featurefly/users/pkg/utils"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
)

func LoginApi(c *gin.Context) {
	var user types.UserRequestV1
	err := c.ShouldBind(&user)
	if err != nil {
		c.String(http.StatusBadRequest, "the user data model does not match the requirements")
	}

	googleAuthEndpoint := "https://oauth2.googleapis.com/tokeninfo"
	mongodb := c.MustGet("mongodb").(*mongo.Database)

	ret, code, err := HandleUserLogin(
		mongodb,
		googleAuthEndpoint,
		user,
		utils.HttpRequest,
		utils.DecodeGoogleAuthToken,
		db.GetUserFromDbByUserEmail,
		utils.GenerateJWT,
		populateResponse)
	if err != nil {
		// TODO should set the error code according to the error type
		c.String(code, err.Error())
	}
	c.JSON(code, ret)
}
