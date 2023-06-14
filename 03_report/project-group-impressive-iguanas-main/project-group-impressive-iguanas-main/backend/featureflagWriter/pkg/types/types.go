package types

import jwt "github.com/golang-jwt/jwt/v5"

type Event interface {
	Event() interface{}
	GenerateKey() string
	GetType() string
}

type UserJwt struct {
	Email string `json:"email"`
	jwt.RegisteredClaims
}

type CreateFeatureRequestV1 struct {
	Email           string `json:"email"`
	ProjectId       string `json:"projectId"`
	Env             string `json:"env"`
	FeatureflagName string `json:"featureflagName"`
}
type CreateCollectionRequestV1 struct {
	Email     string `json:"email"`
	ProjectId string `json:"projectId"`
	Env       string `json:"env"`
}

type UpdateFeatureflagRequestV1 struct {
	Email           string `json:"email,omitempty" bson:"email,omitempty"`
	ProjectId       string `json:"projectId,omitempty" bson:"projectId,omitempty"`
	Env             string `json:"env,omitempty" bson:"env,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty" bson:"featureflagName,omitempty"`
	Status          bool   `json:"status,omitempty" bson:"status,omitempty"`
}

type DeleteFeatureflagRequestV1 struct {
	Email           string `json:"email"`
	ProjectId       string `json:"projectId"`
	Env             string `json:"env"`
	FeatureflagName string `json:"featureflagName"`
}
