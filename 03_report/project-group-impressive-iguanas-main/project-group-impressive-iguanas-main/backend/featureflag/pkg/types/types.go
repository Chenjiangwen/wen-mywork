package types

import jwt "github.com/golang-jwt/jwt/v5"

type UserJwt struct {
	Email string `json:"email"`
	jwt.RegisteredClaims
}

type QueryRequestV1 struct {
	ProjectId string `json:"ProjectId"`
	Env       string `json:"env"`
	Email     string `json:"email"`
}

type QueryResponseV1 struct {
	Featureflags []Featureflag `json:"featureflags"`
}

type CreateFeatureRequestV1 struct {
	ProjectId       string `json:"ProjectId"`
	Env             string `json:"env"`
	FeatureflagName string `json:"featureflagName"`
}

type Featureflag struct {
	// Name string `json:"name"`
	Name   string `json:"name" bson:"name"`
	Status bool   `json:"status" bson:"status" `
}

type FeatureflagSet struct {
	Id           string        `json:"id" bson:"_id"`
	Email        string        `json:"email" bson:"email"`
	Featureflags []Featureflag `json:"featureflags" bson:"featureflags"`
}

type QueryFeatureflagResponseV1 struct {
}

type EmailPayload struct {
	Email string `json:"email"`
}
