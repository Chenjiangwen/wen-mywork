package db

import (
	"context"

	"github.com/featurefly/users/pkg/consts"
	"github.com/featurefly/users/pkg/types"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

func GetUserFromDbByUserEmail(db *mongo.Database, email string) (types.User, error) {
	user := &types.User{}
	filter := bson.M{"_id": email}
	err := db.Collection(consts.DB_USER_COLLECTION).FindOne(context.TODO(), filter).Decode(&user)
	if err != nil {
		if err == mongo.ErrNoDocuments {
			return *user, err
		}
		return *user, err
	}
	return *user, nil
}
