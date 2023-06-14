package middleware

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/featurefly/users/pkg/consts"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const database string = "users"

func DbConnect(c *gin.Context) {
	// Set client options
	var serverAPI *options.ServerAPIOptions
	var clientOptions *options.ClientOptions
	if os.Getenv("env") != "prod" {
		clientOptions = options.Client().ApplyURI(getConnectionURI())
	} else {
		serverAPI = options.ServerAPI(options.ServerAPIVersion1)
		clientOptions = options.Client().ApplyURI(getConnectionURI()).SetServerAPIOptions(serverAPI)
	}

	// Create a new MongoDB client
	client, err := mongo.Connect(context.Background(), clientOptions)
	if err != nil {
		log.Fatalf("Failed to connect to MongoDB: %s", err)
	}

	// Check the connection
	err = client.Ping(context.Background(), nil)
	if err != nil {
		log.Fatalf("Failed to ping MongoDB: %s", err)
	}

	db := client.Database(database)
	defer client.Disconnect(context.Background())
	// Store the client in the context
	c.Set(consts.MONGODB, db)

	// Call the next middleware
	c.Next()
}

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
