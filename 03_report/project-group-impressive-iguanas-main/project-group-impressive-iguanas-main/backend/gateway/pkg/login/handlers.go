package login

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"

	"github.com/featurefly/gateway/pkg/types"
)

func HandleUserLogin(endpoint string,
	user types.UserLoginRequestV1,
	createHttpPayload func(data interface{}) *bytes.Reader,
	makeHttpRequest func(string, string, *bytes.Reader, string) ([]byte, error, int)) (types.UserResponseV1, error, int) {
	var response types.UserResponseV1
	if user.IDToken == "" {
		return response, errors.New("token is empty"), http.StatusBadRequest
	}
	payload := createHttpPayload(user)

	// TODO: Should implement a retry mechanism
	respBody, err, code := makeHttpRequest("POST", fmt.Sprintf("%s/v1/users/login", endpoint), payload, "")
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return response, err, code
	}
	if isTheRequestFailure(code) {
		return response, err, code
	}
	err = json.Unmarshal(respBody, &response)
	if err != nil {
		log.Println("Error creating response:", err)
		return response, err, http.StatusInternalServerError
	}

	return response, nil, http.StatusOK
}

func isTheRequestFailure(code int) bool {
	if code >= 400 {
		return true
	} else {
		return false
	}
}
