package main

import (
	"context"
	"fmt"
	"github/featurefly/event/pkg/consts"
	"github/featurefly/event/pkg/modules"
	"log"
	"os"

	"cloud.google.com/go/pubsub"
)

func main() {
	ctx := context.Background()
	client, err := pubsub.NewClient(ctx, consts.PROJECT_ID)
	if err != nil {
		fmt.Println("pubsub.NewClient1")
	}
	defer client.Close()
	router := modules.CreateRouter()

	subID := ""
	if env := os.Getenv("env"); env != "prod" {
		subID = "featureflagevent-local-sub"
	} else {
		subID = consts.SUB_ID
	}
	err = client.Subscription(subID).Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
		fmt.Println(msg.Data)
		if module := router.Handlers[msg.Attributes["type"]]; module != nil {
			module.Handler(ctx, msg)
		} else {
			log.Println(fmt.Printf("message can not be decoded: %s", msg.Data))
		}
	})
	if err != nil {
		fmt.Println(err)
	}
}
