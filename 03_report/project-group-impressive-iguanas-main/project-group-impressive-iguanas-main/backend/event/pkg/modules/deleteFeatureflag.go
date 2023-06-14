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

type PubSubDeleteFeatureflagMessage struct {
	Id              string `json:"_id" bson:"_id"`
	Type            string `json:"type,omitempty" bson:"type,omitempty"`
	ProjectId       string `json:"projectId,omitempty" bson:"projectId,omitempty"`
	Env             string `json:"env,omitempty" bson:"env,omitempty"`
	Email           string `json:"email,omitempty" bson:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty" bson:"featureflagName,omitempty"`
	Status          bool   `json:"status" bson:"status"`
}

type DeleteFeatureflag struct {
	Type    string
	Mongodb *mongo.Client
	DbName  string
}

func (d DeleteFeatureflag) Handler(ctx context.Context, msg *pubsub.Message) {
	p := &PubSubDeleteFeatureflagMessage{}
	err := json.Unmarshal(msg.Data, p)
	if err != nil {
		log.Printf("failed to unmarshal JSON data: %s", err.Error())
		msg.Nack()
		return
	}

	collection := d.Mongodb.Database(d.DbName).Collection(consts.COLLECTION)
	filter := bson.M{"_id": generateCollectionID(p.ProjectId, p.Env)}
	statement := bson.M{"$pull": bson.M{"featureflags": bson.M{"name": p.FeatureflagName}}}
	_, err = collection.UpdateOne(ctx, filter, statement)
	if err != nil {
		log.Printf("failed to insert a delete event for project: %s, the error is %s", p.Id, err.Error())
		msg.Nack()
		return
	}

	featureflag := d.Mongodb.Database(d.DbName).Collection(consts.FEATUREFLAG)
	statement = bson.M{"_id": generateFeatureflagID(p.FeatureflagName, p.Env, p.ProjectId)}
	_, err = featureflag.DeleteOne(ctx, statement)
	if err != nil {
		log.Println(err)
		msg.Nack()
		return
	}
	msg.Ack()
}
