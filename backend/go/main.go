package main

import (
	"GO/apiHandlers"
	"fmt"
	"log"
	"net/http"
)

func main() {
	// Assign the handler function to a route
	http.HandleFunc("/api/get-available-dates", apiHandlers.GetAvailableleDates)

	// Start the server on port 8080
	fmt.Println("Server is running on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
