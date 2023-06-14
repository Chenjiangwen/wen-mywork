package middleware

import (
	"context"
	"fmt"
	"github/featurefly/featureflagWrite/pkg/consts"
	"log"
	"os"
	"time"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

func DbConnect(c context.Context) context.Context {
	ctx := context.Background()
	// Set client options
	var serverAPI *options.ServerAPIOptions
	var clientOptions *options.ClientOptions
	if os.Getenv("env") != "prod" {
		clientOptions = options.Client().ApplyURI(getConnectionURI())
	} else {
		serverAPI = options.ServerAPI(options.ServerAPIVersion1)
		clientOptions = options.Client().ApplyURI(getConnectionURI()).SetServerAPIOptions(serverAPI)
	}

	dbCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	// Create a new MongoDB client
	client, err := mongo.Connect(dbCtx, clientOptions)
	if err != nil {
		log.Fatalf("Failed to connect to MongoDB: %s", err)
	}

	// Check the connection
	err = client.Ping(dbCtx, nil)
	if err != nil {
		log.Fatalf("Failed to ping MongoDB: %s", err)
	}

	db := client.Database(consts.DB_NAME)
	// Store the client in the context

	ctx = context.WithValue(ctx, consts.MONGODB, db)
	// Call the next middleware
	return ctx
}

func getConnectionURI() string {
	env := os.Getenv("env")
	hostname := os.Getenv("hostname")
	if env != "prod" {
		return fmt.Sprintf("mongodb://%s:27017,%s:27018,%s:27019/dbname?replicaSet=rs", hostname, hostname, hostname)
	} else {
		userDB := os.Getenv("dbUser")
		passwordDB := os.Getenv("dbPassword")
		fmt.Println(userDB)
		fmt.Println(passwordDB)
		return fmt.Sprintf("mongodb+srv://%s:%s@generaldb-pri.15rc8.mongodb.net/?retryWrites=true&w=majority", userDB, passwordDB)
	}

}
