package main

import (
	"server/routes"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	routes.CreateRouter(r)
	r.Run()
}
