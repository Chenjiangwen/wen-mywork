package featureflagAdmin

import (
	"context"
	"fmt"
	"github/featurefly/featureflag/pkg/types"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func getFeatureflagSet(collection *mongo.Collection, request types.QueryRequestV1, email string) (types.FeatureflagSet, error) {
	queryResult := &types.FeatureflagSet{}
	err := collection.FindOne(context.Background(), bson.M{"_id": fmt.Sprintf("%s:%s", request.ProjectId, request.Env), "email": email}).Decode(queryResult)
	return *queryResult, err
}
