import requests
from datetime import datetime

from app.internal_api.serializers import AvailableDatesSerializer


GO_API_URL = "http://localhost:8080/api"


def get_available_dates_for_unit(request_dates: list[datetime.date], suitable_dates: list[datetime.date], days: int) -> requests.Response:
    payload = {
        "days": days,
        "request_dates": request_dates,
        "suitable_dates": suitable_dates,
    }
    serializer = AvailableDatesSerializer(data=payload)
    if serializer.is_valid():
        print(f"Sending request: GetAvailableDates to {GO_API_URL}")
        return requests.post(url=GO_API_URL+"/get-available-dates", json=serializer.data)
    raise requests.Response(serializer.errors, status=400)
        