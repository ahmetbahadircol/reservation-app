from django.contrib import admin
from django.urls import include, path

from app.views import (
    BookingListView,
    BookingView,
    CarListView,
    CarView,
    HotelListView,
    HotelView,
    MultiBookingCreateView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO: Handle homepage
    # path("", views.homepage, name="homepage"),
    path("accounts/", include("accounts.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/hotels", HotelListView.as_view(), name="hotels_list"),
    path("api/hotels/<str:uuid>", HotelView.as_view(), name="hotel"),
    path("api/cars", CarListView.as_view(), name="cars_list"),
    path("api/cars/<str:uuid>", CarView.as_view(), name="car"),
    path("api/bookings", BookingListView.as_view(), name="booking_list"),
    path("api/bookings/<str:uuid>", BookingView.as_view(), name="booking"),
    path("api/bulk-bookings", MultiBookingCreateView.as_view(), name="bulk_bookings"),
]
