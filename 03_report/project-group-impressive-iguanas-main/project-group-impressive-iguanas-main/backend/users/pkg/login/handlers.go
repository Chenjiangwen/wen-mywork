package login

import (
	"bytes"
	"errors"
	"log"
	"net/http"

	"github.com/featurefly/users/pkg/types"
	"go.mongodb.org/mongo-driver/mongo"
)

func HandleUserLogin(
	db *mongo.Database,
	googleAuthEndpoint string,
	userLoginRequestV1 types.UserRequestV1,
	makeHttpRequest func(string, string, *bytes.Reader) ([]byte, error),
	decodeGoogleAuthToken func(string, string, func(string, string, *bytes.Reader) ([]byte, error)) (types.GoogleAuthResponse, error),
	getUserFromDbByUserEmail func(*mongo.Database, string) (types.User, error),
	generateJWT func(string) (string, string, error),
	populateResponse func(types.UserResponseV1, string, []types.Project, func(string) (string, string, error)) (types.UserResponseV1, int, error),
) (
	types.UserResponseV1, int, error) {

	var response types.UserResponseV1
	var userTokenDecoded types.GoogleAuthResponse

	if userLoginRequestV1.IDToken == "" {
		return response, http.StatusBadRequest, errors.New("token is empty")
	}
	userTokenDecoded, err := decodeGoogleAuthToken(userLoginRequestV1.IDToken, googleAuthEndpoint, makeHttpRequest)
	if err != nil {
		log.Println(err)
		return response, http.StatusUnauthorized, err
	}

	user, err := getUserFromDbByUserEmail(db, userTokenDecoded.Email)
	if err != nil {
		if err != mongo.ErrNoDocuments {
			log.Println("mongo connection error", err)
			return response, http.StatusInternalServerError, err
		}
		response, code, err := populateResponse(response, userTokenDecoded.Email, user.Projects, generateJWT)
		if err != nil {
			log.Println(err)
			return response, code, err
		}
		return response, code, nil
	}

	response, code, err := populateResponse(response, user.Email, user.Projects, generateJWT)
	if err != nil {
		log.Println(err)
		return response, code, err
	}
	return response, code, nil
}
