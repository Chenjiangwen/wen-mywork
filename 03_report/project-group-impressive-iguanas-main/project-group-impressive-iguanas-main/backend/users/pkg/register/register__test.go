package register

import (
	"net/http"
	"reflect"
	"testing"

	"github.com/featurefly/users/pkg/types"
	"go.mongodb.org/mongo-driver/mongo"
)

func TestHandleUserRegister(t *testing.T) {
	// Create a mock database
	mockDB := &mongo.Database{}

	// Define mock functions
	getUserFromDbByUserEmail := func(db *mongo.Database, email string) (types.User, error) {
		return types.User{}, nil
	}

	checkIfUserExists := func(user types.User, err error) (bool, error) {
		return false, nil
	}

	insertAUser := func(db *mongo.Database, request types.UserRegisterRequestV1, id string) (types.User, error) {
		return types.User{Email: request.Email, Projects: []types.Project{{Name: request.Name, ID: id, Envs: []string{}}}}, nil
	}

	generateProjectID := func(db *mongo.Database, name string) (string, error) {
		return "project123", nil
	}

	// Define the test case
	testRequest := types.UserRegisterRequestV1{Name: "John Doe", Email: "john.doe@example.com"}
	expectedResponse := types.User{Email: "john.doe@example.com", Projects: []types.Project{{Name: "John Doe", ID: "project123", Envs: []string{}}}}
	expectedStatusCode := http.StatusOK

	// Call the function being tested
	response, err, statusCode := HandleUserRegister(mockDB, testRequest, getUserFromDbByUserEmail, checkIfUserExists, insertAUser, generateProjectID)

	// Check the response
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if statusCode != expectedStatusCode {
		t.Errorf("Unexpected status code: got %v, want %v", statusCode, expectedStatusCode)
	}
	if !reflect.DeepEqual(response, expectedResponse) {
		t.Errorf("Unexpected response: got %v, want %v", response, expectedResponse)
	}
}
