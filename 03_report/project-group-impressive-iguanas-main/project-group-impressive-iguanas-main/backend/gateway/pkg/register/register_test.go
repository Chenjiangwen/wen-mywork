package register

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/featurefly/gateway/pkg/types"
	"github.com/featurefly/gateway/pkg/utils"
)

// Define a mock HTTP server that returns a fixed response
func mockHTTPServer(responseCode int, responseBody string) *httptest.Server {
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(responseCode)
		w.Write([]byte(responseBody))
	})

	return httptest.NewServer(handler)
}

func TestCreateHttpPayload(t *testing.T) {
	// Create a mock user registration request
	user := types.UserRegisterRequestV1{
		Name:  "name",
		Email: "email",
	}

	// Call the function being tested
	payload := utils.CreateHttpPayload(user)

	content, err := ioutil.ReadAll(payload)
	if err != nil {
		t.Errorf("Error during HTTP request: %s", err)
		return
	}
	result := string(content)
	// Assert that the payload is correct
	expectedPayload := "{\"name\":\"name\",\"email\":\"email\"}"
	if result != expectedPayload {
		t.Errorf("Payload did not match expected value. Expected: %s", expectedPayload)
	}
}
func TestHandleUserRegister(t *testing.T) {
	// Define mock variables

	user := types.UserRegisterRequestV1{Name: "name",
		Email: "email"}
	expectedResponse := types.UserRegisterResponseV1{Email: "email", Projects: []types.Project{
		{
			Name: "projectA",
			ID:   "projectA-ID",
			Envs: []string{"env"},
		},
	}}

	// Define mock functions
	createHttpPayload := func(data interface{}) *bytes.Reader {
		payload := bytes.NewReader([]byte("test"))
		return payload
	}
	makeHttpRequest := func(method string, endpoint string, payload *bytes.Reader, auth string) ([]byte, error, int) {
		// Mock HTTP request to return expected response
		result, err := json.Marshal(expectedResponse)
		if err != nil {
			t.Errorf("HandleUserLogin returned an error: %v", err)
		}
		return result, nil, 200
	}
	endpoint := ""
	// Call the function being tested
	response, err, code := handleUserRegister(endpoint, user, createHttpPayload, makeHttpRequest)
	// Check the response and error
	if code < 200 || code > 300 {
		t.Errorf("Error during HTTP request: %s", err)
	}

	if err != nil {
		t.Errorf("HandleUserRegister returned an error: %v", err)
	}
	if response.Email != expectedResponse.Email {
		t.Errorf("HandleUserRegister returned an error: %v", err)
	}
}
