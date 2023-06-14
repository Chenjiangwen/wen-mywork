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

func HttpRequest(method string, endpoint string, payload *bytes.Reader) ([]byte, error) {
	client := &http.Client{}
	var req *http.Request
	var err error
	if payload == nil {
		req, err = http.NewRequest(method, endpoint, nil)
	} else {
		req, err = http.NewRequest(method, endpoint, payload)
	}
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return nil, err
	}
	req.Header.Add("Accept", "application/json")
	req.Header.Set("Content-Type", "application/json")

	// Make the request
	resp, err := client.Do(req)
	if err != nil {
		log.Println("Error sending HTTP request:", err)
		return nil, err
	}
	defer resp.Body.Close()

	// Read the response body
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Println("Error reading response body:", err)
		return nil, err
	}

	return body, err
}
