package main

import (
	"fmt"
	"goAPI/Auth"
	"goAPI/apiHandlers"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/api/get-available-dates", apiHandlers.GetAvailableleDates)
	http.HandleFunc("/protected", Auth.ProtectedEndpoint)

	fmt.Println("Server is running on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
