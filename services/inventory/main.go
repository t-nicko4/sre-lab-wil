
package main

import "github.com/gin-gonic/gin"

func main() {
  r := gin.Default()
  items := []map[string]any{
    {"id": 201, "name": "Laptop", "stock": 5},
    {"id": 202, "name": "Headset", "stock": 12},
  }
  r.GET("/health", func(c *gin.Context) { c.JSON(200, gin.H{"status": "ok"}) })
  r.GET("/items", func(c *gin.Context) { c.JSON(200, items) })
  r.Run(":8002")
}