package modules

import "fmt"

func generateCollectionID(projectId string, env string) string {
	return fmt.Sprintf("%s:%s", projectId, env)
}

func generateFeatureflagID(ff string, env string, projectId string) string {
	return fmt.Sprintf("%s:%s:%s", ff, env, projectId)
}
