package types

import (
	"fmt"
	"github/featurefly/featureflagWrite/pkg/consts"
)

type CreateFeatureflag struct {
	ProjectId       string `json:"projectId,omitempty"`
	Env             string `json:"env,omitempty"`
	Email           string `json:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty"`
	Status          bool   `json:"status"`
	Time            string `json:"time,omitempty"`
	Type            string `json:"type,omitempty"`
}

type PubSubCreateFeatureflagMessage struct {
	Id              string `json:"_id" bson:"_id"`
	Type            string `json:"type,omitempty" bson:"type,omitempty"`
	ProjectId       string `json:"projectId,omitempty" bson:"projectId,omitempty"`
	Env             string `json:"env,omitempty" bson:"env,omitempty"`
	Email           string `json:"email,omitempty" bson:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty" bson:"featureflagName,omitempty"`
	Status          bool   `json:"status" bson:"status"`
}

type DeleteFeatureflag struct {
	ProjectId       string `json:"projectId,omitempty"`
	Env             string `json:"env,omitempty"`
	Email           string `json:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty"`
	Status          bool   `json:"status"`
	Time            string `json:"time,omitempty"`
	Type            string `json:"type,omitempty"`
}

type PubSubDeleteFeatureflagMessage struct {
	Id              string `json:"_id" bson:"_id"`
	Type            string `json:"type,omitempty" bson:"type,omitempty"`
	ProjectId       string `json:"projectId,omitempty" bson:"projectId,omitempty"`
	Env             string `json:"env,omitempty" bson:"env,omitempty"`
	Email           string `json:"email,omitempty" bson:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty" bson:"featureflagName,omitempty"`
	Status          bool   `json:"status" bson:"status"`
}

func (f CreateFeatureflag) Event() interface{} {
	return PubSubCreateFeatureflagMessage{
		Id:              f.GenerateKey(),
		Type:            consts.CREATE_FEATUREFLAG,
		ProjectId:       f.ProjectId,
		Env:             f.Env,
		Email:           f.Email,
		FeatureflagName: f.FeatureflagName,
		Status:          false,
	}
}

func (d DeleteFeatureflag) Event() interface{} {
	return PubSubDeleteFeatureflagMessage{
		Id:              d.GenerateKey(),
		Type:            consts.DELETE_FEATUREFLAG,
		ProjectId:       d.ProjectId,
		Env:             d.Env,
		Email:           d.Email,
		FeatureflagName: d.FeatureflagName,
		Status:          false,
	}
}

func (f CreateFeatureflag) GenerateKey() string {
	return fmt.Sprintf("%s:%s:%s", f.FeatureflagName, f.Env, f.ProjectId)
}

func (f CreateFeatureflag) GetType() string {
	return f.Type
}

func (d DeleteFeatureflag) GenerateKey() string {
	return fmt.Sprintf("%s:%s:%s", d.FeatureflagName, d.Env, d.ProjectId)
}

func (d DeleteFeatureflag) GetType() string {
	return d.Type
}

type UpdateFeatureflag struct {
	ProjectId       string `json:"projectId,omitempty"`
	Env             string `json:"env,omitempty"`
	Email           string `json:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty"`
	Status          bool   `json:"status,omitempty"`
	Time            string `json:"time,omitempty"`
	Type            string `json:"type,omitempty"`
}

type PubSubUpdateFeatureflagMessage struct {
	Id              string `json:"_id" bson:"_id"`
	Type            string `json:"type,omitempty" bson:"type,omitempty"`
	ProjectId       string `json:"projectId,omitempty" bson:"projectId,omitempty"`
	Env             string `json:"env,omitempty" bson:"env,omitempty"`
	Email           string `json:"email,omitempty" bson:"email,omitempty"`
	FeatureflagName string `json:"featureflagName,omitempty" bson:"featureflagName,omitempty"`
	Status          bool   `json:"status" bson:"status"`
}

func (f UpdateFeatureflag) Event() interface{} {
	return PubSubCreateFeatureflagMessage{
		Id:              f.GenerateKey(),
		Type:            consts.UPDATE_FEATUREFLAG,
		ProjectId:       f.ProjectId,
		Env:             f.Env,
		Email:           f.Email,
		FeatureflagName: f.FeatureflagName,
		Status:          f.Status,
	}
}

func (f UpdateFeatureflag) GenerateKey() string {
	return fmt.Sprintf("%s:%s:%s", f.FeatureflagName, f.Env, f.ProjectId)
}

func (f UpdateFeatureflag) GetType() string {
	return f.Type
}
