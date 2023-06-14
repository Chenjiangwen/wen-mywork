package middleware

import (
	"context"
	"github/featurefly/featureflagWrite/pkg/consts"
	"log"
	"os"

	"cloud.google.com/go/pubsub"
)

func PubsubConnect(ctx context.Context) context.Context {
	client, err := pubsub.NewClient(ctx, consts.PROJECT_ID)
	if err != nil {
		log.Fatal(err)
	}
	// defer client.Close()
	env := os.Getenv("env")
	topicName := ""
	if env != "prod" {
		topicName = consts.TOPIC_NAME_TEST
	} else {
		topicName = consts.TOPIC_NAME
	}
	topic := client.Topic(topicName)

	exists, err := topic.Exists(ctx)
	if err != nil {
		log.Fatal(err)
	}

	if !exists {
		log.Printf("Topic %v doesn't exist - creating it", consts.TOPIC_NAME)
		_, err = client.CreateTopic(ctx, consts.TOPIC_NAME)
		if err != nil {
			log.Fatal(err)
		}
	}
	ctx = context.WithValue(ctx, consts.TOPIC_NAME, topic)
	return ctx
}
