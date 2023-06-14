package register

import (
	"log"
	"net/http"

	"github.com/featurefly/users/pkg/types"
	"go.mongodb.org/mongo-driver/mongo"
)

func HandleUserRegister(
	db *mongo.Database,
	request types.UserRegisterRequestV1,
	getUserFromDbByUserEmail func(*mongo.Database, string) (types.User, error),
	checkIfUserExists func(types.User, error) (bool, error),
	insertAUser func(*mongo.Database, types.UserRegisterRequestV1, string) (types.User, error),
	generateProjectID func(*mongo.Database, string) (string, error),
) (
	types.User, error, int) {

	var response types.User
	isExists, err := checkIfUserExists(getUserFromDbByUserEmail(db, request.Email))
	if err != nil {
		log.Println(err)
		return response, err, http.StatusInternalServerError
	}
	if isExists {
		return response, nil, http.StatusConflict
	}

	id, err := generateProjectID(db, request.Name)
	if err != nil {
		log.Println(err)
		return response, err, http.StatusInternalServerError
	}

	response, err = insertAUser(db, request, id)
	if err != nil {
		log.Println(err)
		return response, err, http.StatusInternalServerError
	}

	return response, nil, http.StatusOK
}
