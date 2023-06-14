package featureflags

// TODO: if it has to be upper case then it needs to be moved to the types.go
type RedisConfig struct {
	Addr     string
	Password string
	DB       int
}

// TODO: if it has to be upper case then it needs to be moved to the types.go
type FindFeatureResponse struct {
	Name   string `json:"name"`
	Status bool   `json:"status"`
}

// TODO: if it has to be upper case then it needs to be moved to the types.go
// TODO: if it only contains []FindFeatureResponse, it is better to use []FindFeatureResponse directly
type FindFeaturesResponse struct {
	Featureflags []FindFeatureResponse `json:"featureflags"`
}

// TODO: if it has to be upper case then it needs to be moved to the types.go
type DeleteFeatureflagRequestV1 struct {
	Email string `json:"email"`
	Id    string `json:"id"`
}

type EmailPayload struct {
	Email string `json:"email"`
}

// TODO: if it has to be upper case then it needs to be moved to the types.go
type UpdateFeatureflagRequestV1 struct {
	ProjectId       string `json:"projectId"`
	Env             string `json:"env"`
	FeatureflagName string `json:"featureflagName"`
	Email           string `json:"email"`
	Status          bool   `json:"status"`
}

type createFeatureflagRequestV1 struct {
	ProjectId       string `json:"projectId"`
	Env             string `json:"env"`
	FeatureflagName string `json:"featureflagName"`
	Email           string `json:"email"`
}

type featureflagDeleteRequest struct {
	ProjectId       string `json:"projectId"`
	Env             string `json:"env"`
	FeatureflagName string `json:"featureflagName"`
	Email           string `json:"email"`
}
type featureflagResponseSingle struct {
	Id     string `json:"id"`
	Status bool   `json:"status"`
}
