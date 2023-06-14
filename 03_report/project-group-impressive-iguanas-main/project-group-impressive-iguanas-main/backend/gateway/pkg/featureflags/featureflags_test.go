package featureflags

import (
	"bytes"
	"net/http"
	"testing"

	"github.com/featurefly/gateway/pkg/utils"
)

func TestHandleCreateFeatureflag(t *testing.T) {
	// Define the test data
	endpoint := "http://localhost:8080"
	request := createFeatureflagRequestV1{
		ProjectId:       "project-123",
		Env:             "production",
		FeatureflagName: "new-feature-flag",
		Email:           "test@example.com",
	}

	makeHttpRequest := func(method string, url string, payload *bytes.Reader, token string) ([]byte, error, int) {
		return []byte{}, nil, http.StatusCreated
	}

	// Call the function being tested
	err, code := HandleCreateFeatureflag(endpoint, request, utils.CreateHttpPayload, makeHttpRequest)

	// Check the response
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if code != http.StatusCreated {
		t.Errorf("Expected code %d, but got %d", http.StatusCreated, code)
	}
}

func TestHandleUpdateFeatureflag(t *testing.T) {
	// Define the test data
	endpoint := "http://localhost:8080"
	request := UpdateFeatureflagRequestV1{
		ProjectId:       "project-123",
		Env:             "production",
		FeatureflagName: "new-feature-flag",
		Email:           "test@example.com",
		Status:          true,
	}

	makeHttpRequest := func(method string, url string, payload *bytes.Reader, token string) ([]byte, error, int) {
		return []byte{}, nil, http.StatusCreated
	}

	// Call the function being tested
	err, code := handleUpdateFeatureFlag(endpoint, request, utils.CreateHttpPayload, makeHttpRequest)

	// Check the response
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}
	if code != http.StatusAccepted {
		t.Errorf("Expected code %d, but got %d", http.StatusCreated, code)
	}
}
