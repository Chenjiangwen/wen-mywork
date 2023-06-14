package types

import (
	"fmt"
	"github/featurefly/featureflagWrite/pkg/consts"
)

type CreateCollection struct {
	Email     string `json:"email" bson:"email"`
	ProjectId string `json:"projectId" bson:"projectId"`
	Env       string `json:"env" bson:"env"`
	Time      string `json:"Time" bson:"Time"`
	Type      string `json:"type" bson:"type"`
}

type PubSubCreateCollectionMessage struct {
	Type      string `json:"type" bson:"type"`
	Id        string `json:"_id" bson:"_id"`
	Email     string `json:"email" bson:"email"`
	ProjectId string `json:"projectId" bson:"projectId"`
	Env       string `json:"env" bson:"env"`
	Time      string `json:"Time" bson:"Time"`
}

type DeleteFeatureflagCollection struct {
	Type      string `json:"type" bson:"type"`
	Id        string `json:"_id" bson:"_id"`
	Email     string `json:"email" bson:"email"`
	ProjectId string `json:"projectId" bson:"projectId"`
	Env       string `json:"env" bson:"env"`
	Time      string `json:"Time" bson:"Time"`
}

func (c CreateCollection) Event() interface{} {
	return PubSubCreateCollectionMessage{
		Id:        c.GenerateKey(),
		Email:     c.Email,
		ProjectId: c.ProjectId,
		Env:       c.Env,
		Time:      c.Time,
		Type:      consts.CREATE_COLLECTION,
	}
}

func (c CreateCollection) GenerateKey() string {
	return fmt.Sprintf("%s:%s", c.ProjectId, c.Env)
}
func (c CreateCollection) GetType() string {
	return c.Type
}

func (d DeleteFeatureflagCollection) Event() interface{} {
	return DeleteFeatureflagCollection{
		Id:        d.GenerateKey(),
		Email:     d.Email,
		ProjectId: d.ProjectId,
		Env:       d.Env,
		Time:      d.Time,
		Type:      consts.DELETE_COLLECTION,
	}
}

func (d DeleteFeatureflagCollection) GenerateKey() string {
	return fmt.Sprintf("%s:%s", d.ProjectId, d.Env)
}

func (d DeleteFeatureflagCollection) GetType() string {
	return d.Type
}
