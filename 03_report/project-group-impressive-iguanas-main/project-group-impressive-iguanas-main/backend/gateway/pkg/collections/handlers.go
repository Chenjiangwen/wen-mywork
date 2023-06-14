package collections

import (
	"bytes"
	"fmt"
	"log"
	"net/http"
)

func HandleCreateCollection(endpoint string, request CreateCollectionRequestV1, createHttpPayload func(data interface{}) *bytes.Reader,
	makeHttpRequest func(string, string, *bytes.Reader, string) ([]byte, error, int)) (error, int) {

	payload := createHttpPayload(request)

	//TODO: Should implement a retry mechanism
	_, err, code := makeHttpRequest("POST", fmt.Sprintf("%s/v1/collection/", endpoint), payload, "")
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return err, http.StatusBadRequest
	}

	//TODO: should check if it 200, 201 or 202
	if code >= 400 {
		return err, code
	}

	return nil, http.StatusCreated
}
