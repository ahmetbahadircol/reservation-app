package apiHandlers

import (
	"encoding/json"
	"net/http"
)

type RequestBody struct {
	DaysRange     int      `json:"days_range"`
	RequestDates  []string `json:"request_dates"`
	SuitableDates []string `json:"suitable_dates"`
}

type Response struct {
	FirstDate  string `json:"first_date"`
	SecondDate string `json:"second_date"`
	Message    string `json:"message"`
	MaxDate    string `json:"max_date"`
}

func GetAvailableleDates(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodPost {
		var requestBody RequestBody
		err := json.NewDecoder(r.Body).Decode(&requestBody)
		if err != nil {
			http.Error(w, "Invalid request body", http.StatusBadRequest)
			return
		}

		response := Response{
			FirstDate:  requestBody.RequestDates[0],
			SecondDate: requestBody.RequestDates[len(requestBody.RequestDates)-1], // Last day of slice
			Message:    "Succes!",
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(response)

	} else {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}
