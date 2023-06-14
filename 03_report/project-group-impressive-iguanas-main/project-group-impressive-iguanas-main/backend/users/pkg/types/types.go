package types

import jwt "github.com/golang-jwt/jwt/v5"

type User struct {
	Email    string    `json:"email" bson:"_id"`
	Projects []Project `json:"projects" bson:"projects"`
}
type UserJwt struct {
	Email string `json:"email"`
	jwt.RegisteredClaims
}

type Project struct {
	Name string   `json:"name"`
	ID   string   `json:"id"`
	Envs []string `json:"envs"`
}

type UserRequestV1 struct {
	IDToken string `json:"idToken"`
}

type ProjectID struct {
	ID string `bson:"_id"`
}

type UserRegisterRequestV1 struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

type UserResponseV1 struct {
	User
	Token     string `json:"token"`
	TokenType string `json:"tokenType"`
}

type GoogleAuthResponse struct {
	Iss           string `json:"iss"`
	Azp           string `json:"azp"`
	Aud           string `json:"aud"`
	Sub           string `json:"sub"`
	Email         string `json:"email"`
	EmailVerified bool   `json:"emailVerified"`
	AtHash        string `json:"at_hash"`
	Name          string `json:"name"`
	Picture       string `json:"picture"`
	GivenName     string `json:"given_name"`
	FamilyName    string `json:"family_name"`
	Locale        string `json:"locale"`
	Iat           string `json:"iat"`
	Exp           string `json:"exp"`
	Alg           string `json:"alg"`
	Kid           string `json:"kid"`
	Typ           string `json:"typ"`
}
