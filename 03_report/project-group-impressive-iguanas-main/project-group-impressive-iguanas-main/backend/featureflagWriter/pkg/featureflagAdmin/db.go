package featureflagAdmin

import (
	"context"

	"go.mongodb.org/mongo-driver/mongo"
)

func insertDocument(ctx context.Context, query interface{}, collection *mongo.Collection) error {
	_, err := collection.InsertOne(ctx, query)
	return err
}

func deleteDocument(ctx context.Context, statement interface{}, collection *mongo.Collection) error {
	_, err := collection.DeleteOne(ctx, statement)
	return err
}
func updateDocument(ctx context.Context, query interface{}, update interface{}, collection *mongo.Collection) error {
	// _, err := collection.UpdateByID(ctx, query, update)
	_, err := collection.UpdateOne(ctx, query, update)
	return err
}
func updateOneDocument(ctx context.Context, query interface{}, update interface{}, collection *mongo.Collection) error {
	_, err := collection.UpdateOne(ctx, query, update)
	return err
}

func findOneDocument(ctx context.Context, query interface{}, collection *mongo.Collection) (interface{}, error) {
	var result interface{}
	err := collection.FindOne(ctx, query).Decode(&result)
	return result, err
}
