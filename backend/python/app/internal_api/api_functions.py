import requests
from datetime import date


GO_API_URL = "http://localhost:8080/api"


def get_available_dates_for_unit(request_dates: list[date], suitable_dates: list[date], days: int) -> requests.Response:
    payload = {
        "days": days,
        "request_dates": request_dates,
        "suitable_dates": suitable_dates,
    }
    #serializer = AvailavleDatesSerializer(data=payload)
    return requests.post(url=GO_API_URL+"/get-available-dates", json=payload)