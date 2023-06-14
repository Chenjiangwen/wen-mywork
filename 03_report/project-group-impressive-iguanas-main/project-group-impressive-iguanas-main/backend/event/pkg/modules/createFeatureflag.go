package modules

import (
	"context"
	"encoding/json"
	"github/featurefly/event/pkg/consts"
	"log"

	"cloud.google.com/go/pubsub"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

type PubSubCreateFeatureflagMessage struct {
	Id              string `json:"_id" bson:"_id"`
	Type            string `json:"type,omitempty" bson:"type,omitempty"`
	ProjectId       string `json:"projectId,omitempty" bson:"projectId,omitempty"`
	Env             string `json:"env,omitempty" bson:"env,omitempty"`
	Email           string `json:"email,omitempty" bson:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty" bson:"featureflagName,omitempty"`
	Status          bool   `json:"status" bson:"status"`
}

type CreateFeatureflag struct {
	Type    string
	Mongodb *mongo.Client
	DbName  string
}

// "{\"type\":\"create-collection\",\"_id\":\"dfasddsdfgsf2asdf2:asdfasdf\",\"email\":\"bacfds\",\"projectId\":\"dfasddsdfgsf2asdf2\",\"env\":\"asdfasdf\",\"Time\":\"2023-04-30T12:17:25+12:00\"}"
func (c CreateFeatureflag) Handler(ctx context.Context, msg *pubsub.Message) {
	p := &PubSubCreateFeatureflagMessage{}
	json.Unmarshal(msg.Data, p)
	// this create-featureflag needs two actions, one is to insert the ff to collection, and another one is to insert the ff into the collection that used by users' user.
	collection := c.Mongodb.Database(c.DbName).Collection(consts.COLLECTION)
	filter := bson.M{"_id": generateCollectionID(p.ProjectId, p.Env)}
	statement := bson.M{"$push": bson.M{"featureflags": bson.M{"name": p.FeatureflagName, "status": p.Status}}}
	_, err := collection.UpdateOne(ctx, filter, statement)
	if err != nil {
		log.Println(err)
	}
	featureflag := c.Mongodb.Database(c.DbName).Collection(consts.FEATUREFLAG)
	statement = bson.M{"_id": generateFeatureflagID(p.FeatureflagName, p.Env, p.ProjectId), "status": p.Status}
	_, err = featureflag.InsertOne(ctx, statement)
	if err != nil {
		log.Println(err)
	}
	msg.Ack()
}
