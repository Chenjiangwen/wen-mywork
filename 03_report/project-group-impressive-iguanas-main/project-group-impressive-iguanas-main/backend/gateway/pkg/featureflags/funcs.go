package featureflags

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"strings"

	"github.com/featurefly/gateway/pkg/utils"
	"github.com/gin-gonic/gin"
)

func fLogW(line string) {
	fmt.Println(line)
}

func httpRequest(method string, endpoint string, name string) ([]byte, error) {
	client := &http.Client{}

	rqName := strings.NewReader(name)

	req, err := http.NewRequest(method, endpoint, rqName)
	if err != nil {
		log.Println("Error creating HTTP request:", err)
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")

	// Make the request
	resp, err := client.Do(req)
	if err != nil {
		log.Println("Error sending HTTP request:", err)
		return nil, err
	}
	defer resp.Body.Close()

	// Read the response body
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Println("Error reading response body:", err)
		return nil, err
	}

	return body, err
}

func checkFeatureflagExist(c *gin.Context, ffid string) bool {
	ctx := c.Request.Context()

	//check featureflag exist from mongodb
	endpoint := ctx.Value(utils.FEATUREFLAG_SERVICE).(string)
	// TODO: the function has been a func at the funcs layer (lower layer than handlers), it should not call handlers
	_, err := HandleFeatureFlag(ffid, endpoint, httpRequest)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return false
	}

	return true
}
