package middleware

import (
	"fmt"
	"os"
)

func getConnectionURI() string {
	env := os.Getenv("env")
	hostname := os.Getenv("hostname")
	if env != "prod" {
		return fmt.Sprintf("mongodb://%s:27017,%s:27018,%s:27019/dbname?replicaSet=rs", hostname, hostname, hostname)
	} else {
		userDB := os.Getenv("dbUser")
		passwordDB := os.Getenv("dbPassword")
		return fmt.Sprintf("mongodb+srv://%s:%s@generaldb-pri.15rc8.mongodb.net/?retryWrites=true&w=majority", userDB, passwordDB)
	}

}
