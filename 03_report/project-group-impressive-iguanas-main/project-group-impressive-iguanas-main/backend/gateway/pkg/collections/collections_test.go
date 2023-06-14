package collections

import (
	"bytes"
	"net/http"
	"testing"

	"github.com/featurefly/gateway/pkg/utils"
	"github.com/stretchr/testify/assert"
)

func TestHandleCreateCollection(t *testing.T) {
	endpoint := "http://localhost:8080"
	request := CreateCollectionRequestV1{
		Email:     "test@example.com",
		ProjectId: "project-123",
		Env:       "prod",
	}

	makeHttpRequest := func(method string, url string, payload *bytes.Reader, token string) ([]byte, error, int) {
		return []byte{}, nil, http.StatusCreated
	}

	// Call the function being tested
	err, code := HandleCreateCollection(endpoint, request, utils.CreateHttpPayload, makeHttpRequest)

	// Check the response
	assert.Nil(t, err, "Error should be nil")
	assert.Equal(t, http.StatusCreated, code, "Status code should be http.StatusCreated")
}
