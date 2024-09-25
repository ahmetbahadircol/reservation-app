package apiHandlers

import (
	"bytes"
	"encoding/json"
	"goAPI/apiHandlers"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestGetAvailableleDates_Success(t *testing.T) {
	requestBody := apiHandlers.RequestBody{
		DaysRange:    30,
		RequestDates: []string{"2024-09-01", "2024-09-05"},
		BusyDates:    []string{"2024-08-01", "2024-08-31"},
	}

	jsonBody, err := json.Marshal(requestBody)
	if err != nil {
		t.Fatalf("Could not marshal request body: %v", err)
	}

	req, err := http.NewRequest("POST", "/availableDates", bytes.NewBuffer(jsonBody))
	if err != nil {
		t.Fatalf("Could not create request: %v", err)
	}
	req.Header.Set("Content-Type", "application/json")

	rr := httptest.NewRecorder()

	handler := http.HandlerFunc(apiHandlers.GetAvailableleDates)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("Expected status code 200, got %v", status)
	}

	var resp apiHandlers.Response
	if err := json.NewDecoder(rr.Body).Decode(&resp); err != nil {
		t.Fatalf("Could not decode response: %v", err)
	}

	expectedFirstDate := "2024-09-01"
	expectedSecondDate := "2024-09-05"
	if resp.FirstDate != expectedFirstDate {
		t.Errorf("Expected FirstDate %v, got %v", expectedFirstDate, resp.FirstDate)
	}
	if resp.SecondDate != expectedSecondDate {
		t.Errorf("Expected SecondDate %v, got %v", expectedSecondDate, resp.SecondDate)
	}
	if resp.Message != "Success!" {
		t.Errorf("Expected Message 'Success!', got %v", resp.Message)
	}
}

func TestGetAvailableleDates_RequestDatesNotSorted(t *testing.T) {
	requestBody := apiHandlers.RequestBody{
		DaysRange:    10,
		RequestDates: []string{"2024-09-05", "2024-09-01"},
		BusyDates:    []string{"2024-08-01", "2024-08-31"},
	}

	jsonBody, err := json.Marshal(requestBody)
	if err != nil {
		t.Fatalf("Could not marshal request body: %v", err)
	}

	req, err := http.NewRequest("POST", "/availableDates", bytes.NewBuffer(jsonBody))
	if err != nil {
		t.Fatalf("Could not create request: %v", err)
	}
	req.Header.Set("Content-Type", "application/json")

	rr := httptest.NewRecorder()

	handler := http.HandlerFunc(apiHandlers.GetAvailableleDates)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusBadRequest {
		t.Errorf("Expected status code 400, got %v", status)
	}

	expectedMessage := "{\"error\":\"Request dates are not sorted.\"}"
	if rr.Body.String() != expectedMessage+"\n" {
		t.Errorf("Expected error message %v, got %v", expectedMessage, rr.Body.String())
	}
}

func TestGetAvailableleDates_DatesConflict(t *testing.T) {
	requestBody := apiHandlers.RequestBody{
		DaysRange:    10,
		RequestDates: []string{"2024-08-15", "2024-08-20"},
		BusyDates:    []string{"2024-08-01", "2024-08-31"},
	}

	jsonBody, err := json.Marshal(requestBody)
	if err != nil {
		t.Fatalf("Could not marshal request body: %v", err)
	}

	req, err := http.NewRequest("POST", "/availableDates", bytes.NewBuffer(jsonBody))
	if err != nil {
		t.Fatalf("Could not create request: %v", err)
	}
	req.Header.Set("Content-Type", "application/json")

	rr := httptest.NewRecorder()

	handler := http.HandlerFunc(apiHandlers.GetAvailableleDates)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusBadRequest {
		t.Errorf("Expected status code 400, got %v", status)
	}

	expectedMessage := "{\"error\":\"Suitable and Requested dates overlap.\"}"
	if rr.Body.String() != expectedMessage+"\n" {
		t.Errorf("Expected error message %v, got %v", expectedMessage, rr.Body.String())
	}
}
