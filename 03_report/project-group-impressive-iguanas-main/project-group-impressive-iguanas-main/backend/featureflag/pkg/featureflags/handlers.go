package featureflags

import (
	"net/http"

	"go.mongodb.org/mongo-driver/mongo"
)

func queryHandlerFeatureflag(collection *mongo.Collection,
	request featureflagRequestV1,
	getFeatureflag func(*mongo.Collection, string) (featureflagResponseV1, error)) (featureflagResponseV1, int, error) {

	response := featureflagResponseV1{}
	result, err := getFeatureflag(collection, request.Id)
	if err != nil {
		if err == mongo.ErrNoDocuments {
			return response, http.StatusBadRequest, err
		}
		return response, http.StatusInternalServerError, err
	}
	response = result
	return response, http.StatusOK, nil
}
