package apiHandlers

import (
	"encoding/json"
	"net/http"
	"time"
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

func isSorted(dates []string) (bool, error) {
	layout := "2006-01-02 15:04:05"

	for i := 1; i < len(dates); i++ {
		prev, err := time.Parse(layout, dates[i-1])
		if err != nil {
			return false, err
		}

		curr, err := time.Parse(layout, dates[i])
		if err != nil {
			return false, err
		}

		if prev.After(curr) {
			return false, nil
		}
	}
	return true, nil
}

func validate(w http.ResponseWriter, r *http.Request) {
	var requestBody RequestBody
	err := json.NewDecoder(r.Body).Decode(&requestBody)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	// Validations
	// Check if both dates list is sorted
	flag1, err1 := isSorted(requestBody.RequestDates)
	if err1 != nil {
		http.Error(w, err1.Error(), http.StatusBadRequest)
	}
	if !flag1 {
		http.Error(w, "Request dates are not sorted array", http.StatusBadRequest)
		return
	}

	flag2, err2 := isSorted(requestBody.SuitableDates)
	if err2 != nil {
		http.Error(w, err2.Error(), http.StatusBadRequest)
	}
	if !flag2 {
		http.Error(w, "Suitable dates are not sorted array", http.StatusBadRequest)
		return
	}
}

func GetAvailableleDates(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodPost {
		var requestBody RequestBody

		validate(w, r)

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
