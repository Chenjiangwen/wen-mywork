package utils

import (
	"bytes"
	"encoding/json"
	"io"
	"log"
	"net/http"
)

func CreateHttpPayload(data interface{}) *bytes.Reader {
	marshalled, err := json.Marshal(data)
	if err != nil {
		log.Printf("impossible to marshall teacher: %s", err)
	}
	return bytes.NewReader(marshalled)
}

func HttpRequest(method string, endpoint string, payload *bytes.Reader, authorizationToken string) ([]byte, error, int) {
	client := &http.Client{}

	req, err := http.NewRequest(method, endpoint, payload)
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return nil, err, http.StatusInternalServerError
	}

	req.Close = true
	req.Header.Add("Accept", "application/json")
	req.Header.Set("Content-Type", "application/json")

	if authorizationToken != "" {
		req.Header.Set("authorization", authorizationToken)
	}
	// Make the request
	resp, err := client.Do(req)
	if err != nil {
		log.Println("Error sending HTTP request:", err)
		return nil, err, http.StatusInternalServerError
	}
	defer resp.Body.Close()

	if resp.StatusCode >= 400 {
		return nil, nil, resp.StatusCode
	}

	// Read the response body
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Println("Error reading response body:", err)
		return nil, err, http.StatusInternalServerError
	}

	return body, err, resp.StatusCode
}
