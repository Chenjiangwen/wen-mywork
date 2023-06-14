package featureflags

import (
	"github/featurefly/featureflag/pkg/consts"
	"net/http"

	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
)

func getTheFeatureflag(c *gin.Context) *mongo.Collection {
	mongodb, isExist := c.Get(consts.MONGODB)
	if !isExist {
		c.String(http.StatusInternalServerError, "")
		c.Abort()
	}
	return mongodb.(*mongo.Database).Collection(consts.ADMIN_FEATUREFLAG)
}
