package modules

import (
	"github/featurefly/event/pkg/consts"
	"github/featurefly/event/pkg/db"
)

var (
	CC CreateCollection
	CF CreateFeatureflag
	DF DeleteFeatureflag
	UF UpdateFeatureflag
)

func init() {
	CC = CreateCollection{
		Type:    consts.CREATE_COLLECTION,
		Mongodb: db.Mongodb,
		DbName:  consts.FF_DB_NAME,
	}
	CF = CreateFeatureflag{
		Type:    consts.CREATE_FEATUREFLAG,
		Mongodb: db.Mongodb,
		DbName:  consts.FF_DB_NAME,
	}
	DF = DeleteFeatureflag{
		Type:    consts.DELETE_FEATUREFLAG,
		Mongodb: db.Mongodb,
		DbName:  consts.FF_DB_NAME,
	}
	UF = UpdateFeatureflag{
		Type:    consts.UPDATE_FEATUREFLAG,
		Mongodb: db.Mongodb,
		DbName:  consts.FF_DB_NAME,
	}
}
