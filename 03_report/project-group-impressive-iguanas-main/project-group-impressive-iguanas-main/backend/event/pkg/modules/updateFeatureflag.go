package modules

import (
	"context"
	"encoding/json"
	"fmt"
	"github/featurefly/event/pkg/consts"
	"log"

	"cloud.google.com/go/pubsub"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

type PubSubUpdateFeatureflagMessage struct {
	Id              string `json:"_id" bson:"_id"`
	Type            string `json:"type,omitempty" bson:"type,omitempty"`
	ProjectId       string `json:"projectId,omitempty" bson:"projectId,omitempty"`
	Env             string `json:"env,omitempty" bson:"env,omitempty"`
	Email           string `json:"email,omitempty" bson:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty" bson:"featureflagName,omitempty"`
	Status          bool   `json:"status" bson:"status"`
}

type UpdateFeatureflag struct {
	Type    string
	Mongodb *mongo.Client
	DbName  string
}

func (c UpdateFeatureflag) Handler(ctx context.Context, msg *pubsub.Message) {
	p := &PubSubUpdateFeatureflagMessage{}
	unmarshalErr := json.Unmarshal(msg.Data, p)
	if unmarshalErr != nil {
		log.Printf("failed to unmarshal JSON data: %s", unmarshalErr.Error())
		msg.Nack()
		return
	}
	fmt.Println(p)
	collection := c.Mongodb.Database(c.DbName).Collection(consts.COLLECTION)
	filter := bson.M{"_id": generateCollectionID(p.ProjectId, p.Env), "featureflags.name": p.FeatureflagName}
	statement := bson.M{"$set": bson.M{"featureflags.$.status": p.Status}}
	_, err := collection.UpdateOne(ctx, filter, statement)
	if err != nil {
		log.Println(err)
	}
	featureflag := c.Mongodb.Database(c.DbName).Collection(consts.FEATUREFLAG)
	filter = bson.M{"_id": generateFeatureflagID(p.FeatureflagName, p.Env, p.ProjectId)}
	statement = bson.M{"$set": bson.M{"status": p.Status}}
	_, err = featureflag.UpdateOne(ctx, filter, statement)
	if err != nil {
		log.Println(err)
	}
	msg.Ack()
}
