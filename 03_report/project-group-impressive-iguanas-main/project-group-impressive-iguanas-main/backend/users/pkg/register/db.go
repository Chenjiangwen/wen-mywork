package register

import (
	"context"

	"github.com/featurefly/users/pkg/consts"
	"github.com/featurefly/users/pkg/types"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func insertAUser(db *mongo.Database, request types.UserRegisterRequestV1, projectID string) (types.User, error) {
	result := &types.User{}

	query := bson.M{"_id": request.Email, "projects": []bson.M{
		{"name": request.Name, "id": projectID, "envs": []string{"production", "development"}}}}
	_, err := db.Collection(consts.DB_USER_COLLECTION).InsertOne(context.Background(), query)
	if err != nil {
		return *result, err
	}
	err = convertBsonToStruct(query, result)
	return *result, err
}
