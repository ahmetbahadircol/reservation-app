from .models import Car, Hotel
from rest_framework import serializers


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
        read_only_fields = ["uuid",]


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        read_only_fields = ["uuid",]
