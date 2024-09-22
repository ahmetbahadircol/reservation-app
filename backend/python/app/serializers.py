from .models import Booking, Car, Hotel
from rest_framework import serializers


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
        read_only_fields = ["uuid",]


class HotelSerializer(HotelListSerializer):
    pass


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        read_only_fields = ["uuid",]


class CarSerializer(CarListSerializer):
    pass


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["uuid", "days"]


class BookingSerializer(BookingListSerializer):
    pass
