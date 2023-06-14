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

type PubSubCreateCollectionMessage struct {
	Type      string `json:"type" bson:"type"`
	Id        string `json:"_id" bson:"_id"`
	Email     string `json:"email" bson:"email"`
	ProjectId string `json:"projectId" bson:"projectId"`
	Env       string `json:"env" bson:"env"`
	Time      string `json:"Time" bson:"Time"`
}

type CreateCollection struct {
	Type    string
	Mongodb *mongo.Client
	DbName  string
}

// "{\"type\":\"create-collection\",\"_id\":\"dfasddsdfgsf2asdf2:asdfasdf\",\"email\":\"bacfds\",\"projectId\":\"dfasddsdfgsf2asdf2\",\"env\":\"asdfasdf\",\"Time\":\"2023-04-30T12:17:25+12:00\"}"
func (c CreateCollection) Handler(ctx context.Context, msg *pubsub.Message) {
	p := &PubSubCreateCollectionMessage{}
	json.Unmarshal(msg.Data, p)
	collection := c.Mongodb.Database(c.DbName).Collection(consts.COLLECTION)
	statement := bson.M{"_id": generateCollectionID(p.ProjectId, p.Env), "email": p.Email}
	_, err := collection.InsertOne(ctx, statement)
	if err != nil {
		log.Println(err)
	}
	msg.Ack()
}
