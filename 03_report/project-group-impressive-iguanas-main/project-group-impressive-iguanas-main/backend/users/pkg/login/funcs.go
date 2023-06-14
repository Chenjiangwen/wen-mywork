package login

import (
	"log"
	"net/http"

	"github.com/featurefly/users/pkg/types"
)

func populateResponse(response types.UserResponseV1, email string, projects []types.Project, generateJWT func(string) (string, string, error)) (types.UserResponseV1, int, error) {
	result := types.UserResponseV1{}
	token, tokenType, err := generateJWT(email)
	if err != nil {
		log.Println(err)
		return response, http.StatusInternalServerError, err
	}
	result.Token = token
	result.TokenType = tokenType
	result.Email = email
	result.Projects = projects

	return result, 200, nil
}
