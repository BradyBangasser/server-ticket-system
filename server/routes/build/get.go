package build

import (
	"fmt"
	"net/http"
	"server/models"
	"server/util"

	"github.com/gin-gonic/gin"
)

func GET(c *gin.Context) {
	config, err := util.GetConfig()

	if err != nil {
		c.AbortWithError(http.StatusInternalServerError, err)
	}

	fmt.Println(config)

	buildData := models.ConfigModel{}
	fmt.Println(buildData)
	
	c.JSON(http.StatusOK, config)
}
