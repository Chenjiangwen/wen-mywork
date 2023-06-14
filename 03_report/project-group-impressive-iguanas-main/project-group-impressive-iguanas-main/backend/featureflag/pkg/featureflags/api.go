package featureflags

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func QueryFeatureflagApi(c *gin.Context) {
	request := featureflagRequestV1{
		Id: c.Param("id"),
	}

	if request.Id == "" {
		c.String(http.StatusBadRequest, "")
		c.Abort()
	}

	response, code, err := queryHandlerFeatureflag(getTheFeatureflag(c), request, getFeatureflag)
	if err != nil {
		c.String(code, err.Error())
		c.Abort()
	}
	c.JSON(code, response)
}
