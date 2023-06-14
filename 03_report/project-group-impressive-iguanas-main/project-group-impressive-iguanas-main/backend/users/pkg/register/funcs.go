package register

import (
	"context"
	"fmt"
	"math/rand"
	"strconv"

	"github.com/featurefly/users/pkg/consts"
	"github.com/featurefly/users/pkg/types"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
)

const jwtKey string = "featureflyKey"
const iss string = "featurefly"

func checkIfUserExists(user types.User, err error) (bool, error) {
	if err == nil {
		return true, nil
	}
	if err == mongo.ErrNoDocuments {
		return false, nil
	}
	return false, err
}

func generateProjectID(db *mongo.Database, projectName string) (string, error) {
	projectID := &types.ProjectID{}
	for {
		id := fmt.Sprintf("%s-%s", projectName, generateRandNumber())
		err := db.Collection(consts.DB_PROJECT_ID_COLLECTION).FindOne(context.TODO(), bson.M{"_id": id}).Decode(projectID)
		if err != nil {
			if err == mongo.ErrNoDocuments {
				return id, nil
			}
			return "", err
		}
	}
}

func generateRandNumber() string {
	min := 10000000
	max := 99999999
	randomNum := rand.Intn(max-min+1) + min
	return strconv.Itoa(randomNum)
}

func convertBsonToStruct(query primitive.M, result *types.User) error {
	bsonBytes, err := bson.Marshal(query)
	if err != nil {
		return err
	}

	bson.Unmarshal(bsonBytes, result)
	if err != nil {
		return err
	}
	return nil
}
