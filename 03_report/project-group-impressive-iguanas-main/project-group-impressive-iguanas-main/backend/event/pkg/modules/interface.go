package modules

import (
	"context"

	"cloud.google.com/go/pubsub"
)

type Command interface {
	Handler(ctx context.Context, msg *pubsub.Message)
}
