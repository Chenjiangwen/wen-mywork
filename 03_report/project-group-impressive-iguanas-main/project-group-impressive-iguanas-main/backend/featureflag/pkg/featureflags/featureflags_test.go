package featureflags_test

import (
	"go.mongodb.org/mongo-driver/mongo"

	"github/featurefly/featureflag/pkg/featureflags"
)

type MockedDatabase struct{}

func (db *MockedDatabase) GetFeatureflagById(_ *mongo.Database, id string, collectionName string) (featureflags.Featureflag, error) {
	return featureflags.Featureflag{
		ID:   "test_flag",
		IsOn: true,
	}, nil
}

func (db *MockedDatabase) GetFeatureflags(_ *mongo.Database, id string, collectionName string) (featureflags.Featureflags, error) {
	return featureflags.Featureflags{
		ID:       "test_project:prod",
		Username: "test_user",
		Featureflags: []featureflags.Featureflag{
			{
				ID:   "flag1",
				Name: "Test Feature Flag 1",
				IsOn: true,
			},
			{
				ID:   "flag2",
				Name: "Test Feature Flag 2",
				IsOn: false,
			},
		},
	}, nil
}

//func TestHandleQuery(t *testing.T) {
//	mockDB := &MockedDatabase{}
//	name := "test_flag"
//	collectionName := "featureflag"
//
//	result, err, status := featureflags.HandleQuery(name, collectionName, nil, mockDB.GetFeatureflagById)
//
//	assert.NoError(t, err)
//	assert.Equal(t, http.StatusOK, status)
//	assert.Equal(t, name, result.ID)
//	assert.Equal(t, true, result.IsOn)
//}

//func TestHandleQueryFeatureflags(t *testing.T) {
//	mockDB := &mongo.Database{}
//	mockFeatureflags := featureflags.Featureflags{
//		ID:       "project01:prod",
//		Username: "testuser",
//		Featureflags: []featureflags.Featureflag{
//			{
//				ID:   "flag1",
//				Name: "Test Feature Flag 1",
//				IsOn: true,
//			},
//			{
//				ID:   "flag2",
//				Name: "Test Feature Flag 2",
//				IsOn: false,
//			},
//		},
//	}
//
//	mockGetFeatureflags := func(db *mongo.Database, id, collectionName string) (featureflags.Featureflags, error) {
//		if id == mockFeatureflags.ID {
//			return mockFeatureflags, nil
//		}
//		return featureflags.Featureflags{}, errors.New("featureflags not found")
//	}
//
//	t.Run("success", func(t *testing.T) {
//		response, err, status := featureflags.HandleQueryFeatureflags(mockFeatureflags.ID, "featureflags", mockDB, mockGetFeatureflags)
//		assert.NoError(t, err)
//		assert.Equal(t, http.StatusOK, status)
//		assert.Equal(t, mockFeatureflags.Featureflags, response)
//	})
//
//	t.Run("error", func(t *testing.T) {
//		response, err, status := featureflags.HandleQueryFeatureflags("nonexistent", "featureflags", mockDB, mockGetFeatureflags)
//		assert.Error(t, err)
//		assert.Equal(t, http.StatusInternalServerError, status)
//		assert.Nil(t, response)
//	})
//}
