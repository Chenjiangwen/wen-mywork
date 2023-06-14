package register

import (
	"net/http"

	"github.com/featurefly/users/pkg/consts"
	"github.com/featurefly/users/pkg/db"
	"github.com/featurefly/users/pkg/types"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
)

func RegisterApi(c *gin.Context) {
	var request types.UserRegisterRequestV1

	err := c.ShouldBind(&request)
	if err != nil {
		c.String(http.StatusBadRequest, "the user data model does not match the requirements")
	}

	if request.Name == "" {
		c.String(http.StatusBadRequest, "the project name is not valid")
	}

	mongodb := c.MustGet(consts.MONGODB).(*mongo.Database)

	ret, err, code := HandleUserRegister(
		mongodb,
		request,
		db.GetUserFromDbByUserEmail,
		checkIfUserExists,
		insertAUser,
		generateProjectID,
	)
	if err != nil {
		// TODO should set the error code according to the error type
		c.String(code, err.Error())
	}

	c.JSON(code, ret)
}
