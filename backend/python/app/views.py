from rest_framework import generics, views, response, status
from rest_framework.permissions import AllowAny
from .models import Booking, Car, Hotel
from .serializers import (
    BookingListSerializer,
    BookingSerializer,
    CarListSerializer,
    CarSerializer,
    HotelListSerializer,
    HotelSerializer,
    MultiBookingCreateSerializer,
)
from rest_framework.permissions import IsAuthenticated


class HotelListView(generics.ListCreateAPIView):
    queryset = Hotel.objects.get_queryset()
    serializer_class = HotelListSerializer
    permission_classes = [IsAuthenticated]


class HotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.get_queryset()
    serializer_class = HotelSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    permission_classes = [IsAuthenticated]


class CarListView(generics.ListCreateAPIView):
    queryset = Car.objects.get_queryset()
    serializer_class = CarListSerializer
    permission_classes = [IsAuthenticated]


class CarView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.get_queryset()
    serializer_class = CarSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    permission_classes = [IsAuthenticated]


class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.get_queryset()
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]


class BookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.get_queryset()
    serializer_class = BookingSerializer
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    permission_classes = [IsAuthenticated]


class MultiBookingCreateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser = MultiBookingCreateSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return response.Response(status=status.HTTP_201_CREATED)
        return response.Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
