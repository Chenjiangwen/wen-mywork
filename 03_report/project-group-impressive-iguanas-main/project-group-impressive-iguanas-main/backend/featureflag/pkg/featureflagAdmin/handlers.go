package featureflagAdmin

import (
	"github/featurefly/featureflag/pkg/types"
	"net/http"

	"go.mongodb.org/mongo-driver/mongo"
)

func queryHandler(collection *mongo.Collection, request types.QueryRequestV1, email string, getFeatureflagSet func(*mongo.Collection, types.QueryRequestV1, string) (types.FeatureflagSet, error)) (types.QueryResponseV1, int, error) {
	response := types.QueryResponseV1{}
	result, err := getFeatureflagSet(collection, request, email)
	if err != nil {
		if err == mongo.ErrNoDocuments {
			return response, http.StatusBadRequest, err
		}
		return response, http.StatusInternalServerError, err
	}
	response.Featureflags = result.Featureflags
	return response, http.StatusOK, nil
}
