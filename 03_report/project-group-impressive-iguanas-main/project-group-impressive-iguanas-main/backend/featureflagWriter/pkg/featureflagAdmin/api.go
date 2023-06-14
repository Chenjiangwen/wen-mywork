package featureflagAdmin

import (
	"fmt"
	"github/featurefly/featureflagWrite/pkg/consts"
	"github/featurefly/featureflagWrite/pkg/types"
	"net/http"
	"time"

	"cloud.google.com/go/pubsub"
	"github.com/gin-gonic/gin"
)

func CreateFeatureflagApi(c *gin.Context) {
	request := &types.CreateFeatureRequestV1{}
	if err := c.BindJSON(request); err != nil {
		c.String(http.StatusBadRequest, "")
		c.Abort()
	}

	topic := c.Request.Context().Value(consts.TOPIC_NAME)

	featureflagEvent := types.CreateFeatureflag{
		ProjectId:       request.ProjectId,
		Env:             request.Env,
		Email:           request.Email,
		FeatureflagName: request.FeatureflagName,
		Status:          false,
		Time:            time.Now().Format(time.RFC3339),
		Type:            consts.CREATE_FEATUREFLAG,
	}

	code, err := createFeatureflagHandler(c.Request.Context(), getTheCollection(c, consts.ADMIN_FEATUREFLAG), featureflagEvent, topic.(*pubsub.Topic))
	if err != nil {
		c.String(code, err.Error())
		c.Abort()
	}
	c.String(code, "")

}

func CreateFeatureflagCollectionApi(c *gin.Context) {
	request := &types.CreateCollectionRequestV1{}
	if err := c.BindJSON(request); err != nil {
		c.String(http.StatusBadRequest, "")
		c.Abort()
	}
	topic := c.Request.Context().Value(consts.TOPIC_NAME)
	collection := types.CreateCollection{
		Email:     request.Email,
		ProjectId: request.ProjectId,
		Env:       request.Env,
		Time:      time.Now().Format(time.RFC3339),
		Type:      consts.CREATE_COLLECTION,
	}
	code, err := createCollectionHandler(c.Request.Context(), getTheCollection(c, consts.ADMIN_COLLECTION), collection, topic.(*pubsub.Topic))
	if err != nil {
		c.String(code, err.Error())
		c.Abort()
	}
	c.String(code, "")
}

func UpdateFeatureflagApi(c *gin.Context) {
	request := &types.UpdateFeatureflagRequestV1{}
	if err := c.BindJSON(request); err != nil {
		c.String(http.StatusBadRequest, "")
		c.Abort()
	}

	topic := c.Request.Context().Value(consts.TOPIC_NAME)

	featureFlagEvent := types.UpdateFeatureflag{
		ProjectId:       request.ProjectId,
		Env:             request.Env,
		Email:           request.Email,
		FeatureflagName: request.FeatureflagName,
		Status:          request.Status,
		Time:            time.Now().Format(time.RFC3339),
		Type:            consts.UPDATE_FEATUREFLAG,
	}

	code, err := updateFeatureflagHandler(c.Request.Context(), getTheCollection(c, consts.ADMIN_FEATUREFLAG), featureFlagEvent, topic.(*pubsub.Topic))
	if err != nil {
		c.String(code, err.Error())
		c.Abort()
	}
	c.String(code, "")
}

func DeleteFeatureflagApi(c *gin.Context, request *types.DeleteFeatureflagRequestV1) (int, error) {

	topic := c.Request.Context().Value(consts.TOPIC_NAME)

	featureflagEvent := types.DeleteFeatureflag{
		ProjectId:       request.ProjectId,
		Env:             request.Env,
		Email:           request.Email,
		FeatureflagName: request.FeatureflagName,
		Status:          false,
		Time:            time.Now().Format(time.RFC3339),
		Type:            consts.DELETE_FEATUREFLAG,
	}

	code, err := deleteFeatureflagHandler(c.Request.Context(), getTheCollection(c, consts.ADMIN_FEATUREFLAG), featureflagEvent, topic.(*pubsub.Topic))
	if err != nil {
		c.String(code, err.Error())
		c.Abort()
	}
	return code, nil
}

func DeleFeatureflagCollectionApi(c *gin.Context, request *types.DeleteFeatureflagRequestV1) (int, error) {
	topic := c.Request.Context().Value(consts.TOPIC_NAME)

	featureflagEvent := types.DeleteFeatureflagCollection{
		ProjectId: request.ProjectId,
		Env:       request.Env,
		Email:     request.Email,
		Time:      time.Now().Format(time.RFC3339),
		Type:      consts.DELETE_COLLECTION,
	}
	fmt.Print(featureflagEvent)
	code, err := deleteFeatureflagCollectionHandler(c.Request.Context(), getTheCollection(c, consts.ADMIN_COLLECTION), featureflagEvent, topic.(*pubsub.Topic))
	if err != nil {
		c.String(code, err.Error())
		c.Abort()
	}
	return code, nil
}

func DeleteHandler(c *gin.Context) {

	request := &types.DeleteFeatureflagRequestV1{}
	if err := c.BindJSON(request); err != nil {
		c.String(http.StatusBadRequest, "")
		c.Abort()
		return
	}

	code, err := DeleFeatureflagCollectionApi(c, request)
	if err != nil {
		c.String(code, fmt.Sprintf("Error processing request: %s", err.Error()))
		c.Abort()
		return
	}

	code, err = DeleteFeatureflagApi(c, request)
	if err != nil {
		c.String(code, fmt.Sprintf("Error processing request: %s", err.Error()))
		c.Abort()
		return
	}
	c.JSON(code, "Request processed successfully")
}
