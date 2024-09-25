package utils

import (
	"encoding/json"
	"net/http"
)

func HandleError(w http.ResponseWriter, message string, status int) {
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(map[string]string{"error": message})
}
