package utils

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"strings"

	"github.com/featurefly/users/pkg/types"
)

func DecodeGoogleAuthToken(IDToken string, googleAuthEndpoint string, httpRequest func(string, string, *bytes.Reader) ([]byte, error)) (types.GoogleAuthResponse, error) {
	var userTokenDecoded types.GoogleAuthResponse
	URL := fmt.Sprintf("%s?id_token=%s", googleAuthEndpoint, IDToken)
	respBody, err := httpRequest("GET", URL, nil)
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return userTokenDecoded, err
	}

	err = json.Unmarshal(respBody, &userTokenDecoded)
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return userTokenDecoded, err
	}
	if userTokenDecoded.Email == "" {
		return userTokenDecoded, errors.New("token can not be parsed")
	}

	userTokenDecoded.Email = strings.ToLower(userTokenDecoded.Email)

	return userTokenDecoded, nil
}
