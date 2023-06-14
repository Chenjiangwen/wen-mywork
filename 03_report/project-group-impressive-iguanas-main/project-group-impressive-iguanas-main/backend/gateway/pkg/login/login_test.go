package login

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"reflect"
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
	// Create a mock user login request
	user := types.UserLoginRequestV1{
		IDToken: "1234567890",
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
	expectedPayload := "{\"idToken\":\"1234567890\"}"
	if expectedPayload != result {
		t.Errorf("Payload did not match expected value. Expected: %s, got: %s", expectedPayload, result)
	}
}

func TestHttpRequest(t *testing.T) {
	// Create a mock HTTP server and login endpoint
	mockServer := mockHTTPServer(200, "success")
	defer mockServer.Close()

	endpoint := mockServer.URL

	// Create a mock payload
	payload := bytes.NewReader([]byte("test payload"))

	// Call the function being tested
	responseBody, err, code := utils.HttpRequest("POST", endpoint, payload, "")

	// Assert that the response is correct
	if err != nil {
		t.Errorf("Error during HTTP request: %s", err)
	}
	if code < 200 || code > 300 {
		t.Errorf("Error during HTTP request: %s", err)
	}
	expectedResponseBody := "success"
	if string(responseBody) != expectedResponseBody {
		t.Errorf("Response body did not match expected value. Expected: %s, got: %s", expectedResponseBody, string(responseBody))
	}
}

func TestHandleUserLogin(t *testing.T) {
	// Define mock variables

	user := types.UserLoginRequestV1{IDToken: "idToken123"}
	expectedResponse := types.UserResponseV1{Token: "token123", TokenType: "Bearer",
		Projects: []types.Project{
			{
				Name: "projectA",
				ID:   "projectA-ID",
				Envs: []string{"env"},
			},
		},
	}

	// 	// Define mock functions
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
	response, err, code := HandleUserLogin(endpoint, user, createHttpPayload, makeHttpRequest)
	if code < 200 || code > 300 {
		t.Errorf("Error during HTTP request: %s", err)
	}
	// Check the response and error
	if err != nil {
		t.Errorf("HandleUserLogin returned an error: %v", err)
	}
	if !reflect.DeepEqual(response, expectedResponse) {
		t.Errorf("HandleUserLogin returned an error: %v", err)
	}
}
