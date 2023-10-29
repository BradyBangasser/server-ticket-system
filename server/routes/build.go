package routes

import (
	server_routes_build "server/routes/build"
	server_routes___test__ "server/routes/__test__"
	"github.com/gin-gonic/gin"
)

func CreateRouter(r *gin.Engine) {
	r_build := r.Group("/build"); {
		r_build.GET("/", server_routes_build.GET)
	}
	r___test__ := r.Group("/[test]"); {
		r___test__.GET("/", server_routes___test__.GET)
	}
}
