package collections

type CreateCollectionRequestV1 struct {
	Email     string `json:"email"`
	ProjectId string `json:"projectId"`
	Env       string `json:"env"`
}
