from rest_framework import generics
from .models import Booking, Car, Hotel
from .serializers import BookingListSerializer, BookingSerializer, CarListSerializer, CarSerializer, HotelListSerializer, HotelSerializer


class HotelListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.get_queryset()
    serializer_class = HotelListSerializer


class HotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.get_queryset()
    serializer_class = HotelSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"


class CarListView(generics.ListCreateAPIView):
    queryset = Car.objects.get_queryset()
    serializer_class = CarListSerializer


class CarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.get_queryset()
    serializer_class = CarSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"


class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.get_queryset()
    serializer_class = BookingListSerializer


class BookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.get_queryset()
    serializer_class = BookingSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"