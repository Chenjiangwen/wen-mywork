package collections

import (
	"net/http"

	"github.com/featurefly/gateway/pkg/consts"
	"github.com/featurefly/gateway/pkg/utils"
	"github.com/gin-gonic/gin"
)

func CreateCollection(c *gin.Context) {
	ctx := c.Request.Context()
	request := &CreateCollectionRequestV1{}
	if err := c.BindJSON(request); err != nil {
		c.String(http.StatusBadRequest, "the data model does not match the requirements")
		return
	}

	if request.Env == "" || request.ProjectId == "" {
		c.String(http.StatusBadRequest, "the data model does not match the requirements")
		return
	}

	request.Email = c.Value(consts.USER_JWT_KEY).(string)
	err, code := HandleCreateCollection(ctx.Value(utils.FEATUREFLAG_WRITE_SERVICE).(string), *request, utils.CreateHttpPayload, utils.HttpRequest)
	if err != nil {
		c.String(code, err.Error())
		return
	}
	c.JSON(code, "")
}
