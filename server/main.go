package main

import (
	"server/routes"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.String(200, "pong")
	})

	r.Static("/public", "/public")
	r.GET("/build", routes.GetBuild)

	r.Run()
}
