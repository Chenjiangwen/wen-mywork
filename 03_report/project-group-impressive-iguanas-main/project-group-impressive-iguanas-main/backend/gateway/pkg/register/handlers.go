package register

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"

	"github.com/featurefly/gateway/pkg/types"
)

func handleUserRegister(endpoint string,
	user types.UserRegisterRequestV1,
	createHttpPayload func(data interface{}) *bytes.Reader,
	makeHttpRequest func(string, string, *bytes.Reader, string) ([]byte, error, int)) (types.UserRegisterResponseV1, error, int) {
	var response types.UserRegisterResponseV1

	if user.Name == "" {
		return response, errors.New("Token is empty"), http.StatusBadRequest
	}

	payload := createHttpPayload(user)

	//TODO: Should implement a retry mechanism
	respBody, err, code := makeHttpRequest("POST", fmt.Sprintf("%s/v1/users/register", endpoint), payload, "")
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return response, err, http.StatusBadRequest
	}

	if code >= 400 {
		return response, err, code
	}

	err = json.Unmarshal(respBody, &response)
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return response, err, http.StatusBadRequest
	}
	return response, nil, http.StatusCreated
}
