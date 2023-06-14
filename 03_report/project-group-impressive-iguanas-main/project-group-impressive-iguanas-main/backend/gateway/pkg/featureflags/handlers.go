package featureflags

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strings"

	"github.com/featurefly/gateway/pkg/types"
)

func HandleFeatureFlag(name string, endpoint string,
	makeHttpRequest func(string, string, string) ([]byte, error)) (featureflagResponseSingle, error) {
	var response featureflagResponseSingle
	respBody, err := makeHttpRequest("GET", fmt.Sprintf("%s/v1/featureflags/%s", endpoint, name), name)
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return response, err
	}
	err = json.Unmarshal(respBody, &response)
	if err != nil {
		log.Println("Error unmarshalling JSON response:", err)
		return response, err
	}
	return response, nil
}

// FindFeaturesResponse eg: {Featureflags:[{id: "ffname:projectname:env", name:"ffnameaa", status:true}, {...}, ...]}
func HandleFeatureFlags(projectId string,
	env string,
	email types.EmailPayload,
	endpoint string,
	createHttpPayload func(data interface{}) *bytes.Reader,
	makeHttpRequest func(string, string, *bytes.Reader, string) ([]byte, error, int)) (FindFeaturesResponse, error, int) {
	var response FindFeaturesResponse

	payload := createHttpPayload(email) //TODO

	respBody, err, code := makeHttpRequest("POST", fmt.Sprintf("%s/v1/featureflagAdmin/featureflag/%s/%s", endpoint, projectId, env), payload, "")
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return response, err, code
	}
	err = json.Unmarshal(respBody, &response)
	if err != nil {
		log.Println("Error unmarshalling JSON response:", err)
		return response, err, code
	}
	return response, nil, http.StatusOK

}

// delete featureflag
func handleDeleteFeatureFlag(
	request DeleteFeatureflagRequestV1,
	endpoint string,
	makeHttpRequest func(string, string, string) ([]byte, error)) (int, error) {
	featureflagEnvProject := strings.Split(request.Id, ":")
	requestStruct := featureflagDeleteRequest{
		ProjectId:       featureflagEnvProject[2],
		Env:             featureflagEnvProject[1],
		FeatureflagName: featureflagEnvProject[0],
		Email:           request.Email,
	}
	requestJson, err := json.Marshal(requestStruct)
	if err != nil {
		log.Println("Error marshalling request:", err)
		return http.StatusInternalServerError, err
	}

	respBody, err := makeHttpRequest("DELETE", fmt.Sprintf("%s/v1/featureflag", endpoint), string(requestJson))

	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return http.StatusInternalServerError, err
	}
	var response string

	err = json.Unmarshal(respBody, &response)
	if err != nil {
		log.Println("Error unmarshalling JSON response:", err)
		return http.StatusInternalServerError, err
	}

	return http.StatusOK, nil
}

func handleUpdateFeatureFlag(endpoint string, request UpdateFeatureflagRequestV1, createHttpPayload func(data interface{}) *bytes.Reader,
	makeHttpRequest func(string, string, *bytes.Reader, string) ([]byte, error, int)) (error, int) {
	payload := createHttpPayload(request)
	_, err, code := makeHttpRequest("PATCH", fmt.Sprintf("%s/v1/featureflag/", endpoint), payload, "")
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return err, http.StatusBadRequest
	}
	if code >= 400 {
		return err, code
	}
	return nil, http.StatusAccepted
}

func HandleCreateFeatureflag(endpoint string, request createFeatureflagRequestV1, createHttpPayload func(data interface{}) *bytes.Reader,
	makeHttpRequest func(string, string, *bytes.Reader, string) ([]byte, error, int)) (error, int) {

	payload := createHttpPayload(request)

	//TODO: Should implement a retry mechanism
	_, err, code := makeHttpRequest("POST", fmt.Sprintf("%s/v1/featureflag/", endpoint), payload, "")
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return err, http.StatusBadRequest
	}
	//TODO: should check if it is 200, 201 and 202
	if code >= 400 {
		return err, code
	}

	return nil, http.StatusCreated
}
