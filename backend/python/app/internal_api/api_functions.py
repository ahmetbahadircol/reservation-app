import requests
from datetime import datetime

from app.internal_api.serializers import AvailableDatesSerializer


GO_API_URL = "http://localhost:8080/api"


def call_go_microservice(jwt_token):
    headers = {
        "Authorization": f"Bearer {jwt_token}",  # JWT token'ı header'a ekleyin
    }

    # Go microservice endpoint'ine istek gönderin
    response = requests.get(
        "http://go-microservice-endpoint/protected", headers=headers
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unauthorized"}


def get_available_dates_for_unit(
    request_dates: list[datetime.date], busy_dates: list[datetime.date], days: int
) -> requests.Response:
    print("Sending request ------------")
    payload = {
        "days": days,
        "request_dates": request_dates,
        "busy_dates": busy_dates,
    }
    serializer = AvailableDatesSerializer(data=payload)
    if serializer.is_valid():
        print(f"Sending request: GetAvailableDates to {GO_API_URL}")
        return requests.post(
            url=GO_API_URL + "/get-available-dates", json=serializer.data
        )
    raise requests.Response(serializer.errors, status=400)
