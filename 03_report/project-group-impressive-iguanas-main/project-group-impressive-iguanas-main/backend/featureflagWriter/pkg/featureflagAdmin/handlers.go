package featureflagAdmin

import (
	"context"
	"fmt"
	"github/featurefly/featureflagWrite/pkg/types"
	"log"
	"net/http"

	"cloud.google.com/go/pubsub"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
)

// All validation should be done at the gateway layer
func createFeatureflagHandler(ctx context.Context, collection *mongo.Collection, event types.Event, topic *pubsub.Topic) (int, error) {
	featureflag, err := findOneDocument(ctx, bson.M{"_id": event.GenerateKey()}, collection)
	if err != nil {
		if err != mongo.ErrNoDocuments {
			log.Println(fmt.Sprintf("failed to insert a create event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
			return http.StatusInternalServerError, err
		}
	}
	if featureflag != nil {
		filter := bson.M{"_id": event.GenerateKey()}
		update := bson.M{"$push": bson.M{"event": event.Event()}}
		err := updateOneDocument(ctx, filter, update, collection)
		if err != nil {
			log.Println(fmt.Sprintf("failed to insert a create event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
			return http.StatusInternalServerError, err
		}
	} else {
		query := bson.M{"_id": event.GenerateKey(), "event": []interface{}{event.Event()}}
		err := insertDocument(ctx, query, collection)
		if err != nil {
			log.Println(fmt.Sprintf("failed to insert a create event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
			return http.StatusInternalServerError, err
		}
	}

	err = sendMessageToMessageQueue(ctx, topic, event)
	if err != nil {
		log.Printf("Error at sendMessageToMessageQueue: %s", err)
		// err := deleteDocument(ctx, query, collection)
		// if err != nil {
		// 	log.Println(fmt.Sprintf("failed to delete a create event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
		// }
		return http.StatusInternalServerError, nil
	}

	return http.StatusAccepted, nil
}

func createCollectionHandler(ctx context.Context, collection *mongo.Collection, event types.Event, topic *pubsub.Topic) (int, error) {

	query := bson.M{"_id": event.GenerateKey(), "event": []interface{}{event.Event()}}

	err := insertDocument(ctx, query, collection)
	if err != nil {
		log.Println(fmt.Sprintf("failed to insert a create event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
		return http.StatusInternalServerError, err
	}

	err = sendMessageToMessageQueue(ctx, topic, event)
	if err != nil {
		log.Printf("Error at sendMessageToMessageQueue: %s", err)
		err := deleteDocument(ctx, query, collection)
		if err != nil {
			log.Println(fmt.Sprintf("failed to delete a create event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
		}
		return http.StatusInternalServerError, nil
	}

	return http.StatusAccepted, nil
}

func deleteFeatureflagHandler(ctx context.Context, collection *mongo.Collection, event types.Event, topic *pubsub.Topic) (int, error) {
	filter := bson.M{"_id": event.GenerateKey()}
	update := bson.M{"$push": bson.M{"event": event.Event()}}
	err := updateDocument(ctx, filter, update, collection)
	if err != nil {
		log.Printf("failed to insert a delete event for project: %s, the error is %s", event.GenerateKey(), err.Error())
		return http.StatusInternalServerError, err
	}

	err = sendMessageToMessageQueue(ctx, topic, event)
	if err != nil {
		log.Printf("Error at sendMessageToMessageQueue: %s", err)
		//delete last element from event
		deleteFromEvent := bson.M{"$pop": bson.M{"event": 1}}
		err := updateDocument(ctx, filter, deleteFromEvent, collection)
		if err != nil {
			log.Printf("failed to delete a delete event for project: %s, the error is %s", event.GenerateKey(), err.Error())
		}
		return http.StatusInternalServerError, nil
	}

	return http.StatusAccepted, nil
}

func deleteFeatureflagCollectionHandler(ctx context.Context, collection *mongo.Collection, event types.Event, topic *pubsub.Topic) (int, error) {
	filter := bson.M{"_id": event.GenerateKey()}
	update := bson.M{"$push": bson.M{"event": event.Event()}}
	err := updateDocument(ctx, filter, update, collection)
	if err != nil {
		log.Printf("failed to insert a delete event for project: %s, the error is %s", event.GenerateKey(), err.Error())
		return http.StatusInternalServerError, err
	}
	return http.StatusAccepted, nil
}

func updateFeatureflagHandler(ctx context.Context, collection *mongo.Collection, event types.Event, topic *pubsub.Topic) (int, error) {
	filter := bson.M{"_id": event.GenerateKey()}
	update := bson.M{"$push": bson.M{"event": event.Event()}}
	err := updateOneDocument(ctx, filter, update, collection)
	if err != nil {
		log.Println(fmt.Sprintf("failed to insert a update event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
		return http.StatusInternalServerError, err
	}
	err = sendMessageToMessageQueue(ctx, topic, event)
	if err != nil {
		log.Printf("Error at sendMessageToMessageQueue: %s", err)
		// removes the first or last element of an array. 1 to remove the last element in an array.
		remove := bson.M{"$pop": bson.M{"event": 1}}
		err := updateOneDocument(ctx, filter, remove, collection)
		if err != nil {
			log.Println(fmt.Sprintf("failed to delete a update event for project: %s, the error is %s", event.GenerateKey(), err.Error()))
		}
		return http.StatusInternalServerError, nil
	}

	return http.StatusAccepted, nil
}
