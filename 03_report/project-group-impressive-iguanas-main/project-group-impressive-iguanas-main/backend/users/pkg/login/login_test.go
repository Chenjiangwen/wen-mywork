package login

import (
	"bytes"
	"net/http"
	"testing"

	"github.com/featurefly/users/pkg/types"
	"go.mongodb.org/mongo-driver/mongo"
)

func TestHandleUserLogin(t *testing.T) {
	// create a mock MongoDB database
	db := &mongo.Database{}
	// set up other mock dependencies
	makeHttpRequest := func(method, url string, body *bytes.Reader) ([]byte, error) {
		return []byte{}, nil
	}
	decodeGoogleAuthToken := func(token string, endpoint string, makeRequest func(string, string, *bytes.Reader) ([]byte, error)) (types.GoogleAuthResponse, error) {
		return types.GoogleAuthResponse{}, nil
	}
	getUserFromDbByUserEmail := func(db *mongo.Database, email string) (types.User, error) {
		return types.User{}, nil
	}
	generateJWT := func(email string) (string, string, error) {
		return "", "", nil
	}
	populateResponse := func(resp types.UserResponseV1, email string, projects []types.Project, generateJWT func(string) (string, string, error)) (types.UserResponseV1, int, error) {
		return types.UserResponseV1{}, http.StatusOK, nil
	}

	// create a user login request for testing
	req := types.UserRequestV1{
		IDToken: "some-id-token",
	}

	// call the function being tested
	response, code, err := HandleUserLogin(db, "http://example.com", req, makeHttpRequest, decodeGoogleAuthToken, getUserFromDbByUserEmail, generateJWT, populateResponse)

	// check the response
	if response.Email != "" {
		t.Errorf("Expected email to be empty, but got %v", response.Email)
	}
	if response.Token != "" {
		t.Errorf("Expected token to be empty, but got %v", response.Token)
	}
	if response.TokenType != "" {
		t.Errorf("Expected token type to be empty, but got %v", response.TokenType)
	}
	if code != http.StatusOK {
		t.Errorf("Expected status code %v, but got %v", http.StatusOK, code)
	}
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
}
