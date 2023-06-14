package featureflagAdmin

import (
	"context"
	"encoding/json"
	"fmt"
	"github/featurefly/featureflagWrite/pkg/consts"
	"github/featurefly/featureflagWrite/pkg/types"
	"log"
	"net/http"

	"cloud.google.com/go/pubsub"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
)

func getTheCollection(c *gin.Context, collectionName string) *mongo.Collection {
	ctx := c.Request.Context()
	mongodb := ctx.Value(consts.MONGODB)
	if mongodb == nil {
		c.String(http.StatusInternalServerError, "")
		c.Abort()
	}
	return mongodb.(*mongo.Database).Collection(collectionName)
}

func sendMessageToMessageQueue(ctx context.Context, topic *pubsub.Topic, event types.Event) error {
	jsonMessage, err := json.Marshal(event.Event())
	if err != nil {
		fmt.Printf("Error: %s", err)
	}
	msg := &pubsub.Message{
		Data: []byte(jsonMessage),
		Attributes: map[string]string{
			"type": event.GetType(),
		},
	}

	if _, err := topic.Publish(ctx, msg).Get(ctx); err != nil {
		log.Println(fmt.Sprintf("Could not publish message: %v", err))
		return err
	}
	return nil
}
