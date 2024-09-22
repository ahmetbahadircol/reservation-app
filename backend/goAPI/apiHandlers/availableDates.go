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

var layout = "2006-01-02"

func isSorted(dates []string) (bool, error) {
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

func checkDatesNotConflict(s_dates []string, r_dates []string) (bool, error) {
	s_dates_first, err1 := time.Parse(layout, s_dates[0])
	s_dates_last, err3 := time.Parse(layout, s_dates[len(s_dates)-1])
	r_dates_last, err2 := time.Parse(layout, r_dates[len(r_dates)-1])
	r_dates_first, err4 := time.Parse(layout, r_dates[0])

	if err1 != nil {
		return false, err1
	} else if err2 != nil {
		return false, err2
	} else if err3 != nil {
		return false, err3
	} else if err4 != nil {
		return false, err4
	}
	// Requested dates can be before the sutiable dates
	if r_dates_last.Before(s_dates_first) {
		return true, nil
	}
	// Requested dates can be after the sutiable dates
	if s_dates_last.Before(r_dates_first) {
		return true, nil
	}
	// Requested dates can be between the sutiable dates
	for i := 0; i < len(s_dates)-1; i++ {
		curr, err5 := time.Parse(layout, s_dates[i])
		aft, err6 := time.Parse(layout, s_dates[i+1])

		if err5 != nil {
			return false, err5
		} else if err6 != nil {
			return false, err6
		}

		if curr.Before(r_dates_first) {
			if aft.After(r_dates_last) {
				return true, nil
			}
		}
	}
	return false, nil
}

func validate(w http.ResponseWriter, r *http.Request) (*RequestBody, error) {
	var requestBody RequestBody
	err := json.NewDecoder(r.Body).Decode(&requestBody)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return nil, err
	}

	// Check if both dates list is sorted
	flag1, err1 := isSorted(requestBody.RequestDates)
	if err1 != nil {
		http.Error(w, err1.Error(), http.StatusBadRequest)
		return nil, err1
	}
	if !flag1 {
		http.Error(w, "Request dates are not sorted.", http.StatusBadRequest)
		return nil, nil
	}

	flag2, err2 := isSorted(requestBody.SuitableDates)
	if err2 != nil {
		http.Error(w, err2.Error(), http.StatusBadRequest)
		return nil, err2
	}
	if !flag2 {
		http.Error(w, "Suitable dates are not sorted.", http.StatusBadRequest)
		return nil, nil
	}

	// Check if both dates not conflict
	flag3, err3 := checkDatesNotConflict(requestBody.RequestDates, requestBody.SuitableDates)
	if err3 != nil {
		http.Error(w, err3.Error(), http.StatusBadRequest)
		return nil, err3
	}
	if !flag3 {
		http.Error(w, "Suitable and Requested dates overlap.", http.StatusBadRequest)
		return nil, nil
	}

	return &requestBody, nil
}

func GetAvailableleDates(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodPost {
		requestBody, err := validate(w, r)
		if err != nil || requestBody == nil {
			return
		}

		response := Response{
			FirstDate:  requestBody.RequestDates[0],
			SecondDate: requestBody.RequestDates[len(requestBody.RequestDates)-1], // Last day of slice
			Message:    "Success!",
		}

		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(response)

	} else {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
	}
}
