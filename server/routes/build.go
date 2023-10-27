package routes

import (
	server_routes_build "server/routes/build"
	"github.com/gin-gonic/gin"
)

func CreateRouter(r *gin.Engine) {
	r_build := r.Group("/build"); {
		r_build.GET("/", server_routes_build.GET)
	}
}
