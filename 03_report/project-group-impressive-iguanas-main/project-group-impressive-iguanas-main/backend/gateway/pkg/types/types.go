package types

import jwt "github.com/golang-jwt/jwt/v5"

type UserLoginRequestV1 struct {
	IDToken string `json:"idToken"`
}

type UserRegisterRequestV1 struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

type UserJwt struct {
	Email string `json:"email"`
	jwt.RegisteredClaims
}

type UserResponseV1 struct {
	Email     string    `json:"email"`
	Token     string    `json:"token"`
	TokenType string    `json:"tokenType"`
	Projects  []Project `json:"projects"`
}

type UserRegisterResponseV1 struct {
	Email    string    `json:"email"`
	Projects []Project `json:"projects"`
}

type Project struct {
	Name string   `json:"name"`
	ID   string   `json:"id"`
	Envs []string `json:"envs"`
}

type EmailPayload struct {
	Email string `json:"email"`
}
