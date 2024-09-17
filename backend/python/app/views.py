from rest_framework import generics
from .models import Car, Hotel
from .serializers import CarListSerializer, HotelListSerializer


class HotelListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.get_queryset()
    serializer_class = HotelListSerializer


class CarListView(generics.ListCreateAPIView):
    queryset = Car.objects.get_queryset()
    serializer_class = CarListSerializer