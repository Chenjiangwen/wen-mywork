package featureflags

import (
	"context"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func getFeatureflag(collection *mongo.Collection, id string) (featureflagResponseV1, error) {
	ff := &featureflagResponseV1{}
	err := collection.FindOne(context.Background(), bson.M{"_id": id}).Decode(ff)
	return *ff, err
}
