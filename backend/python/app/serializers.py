from datetime import timedelta, date
from .models import Booking, Car, Hotel, Unit
from rest_framework import serializers
from django.db import transaction


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
    res_date = serializers.DateField()
    class Meta:
        model = Booking
        read_only_fields = ["uuid", "days"]
        fields = ["res_date"] + read_only_fields


class BookingSerializer(BookingListSerializer):
    pass


class MultiBookingCreateSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    unit = serializers.IntegerField()

    class Meta:
        fields = "__all__"
        read_only_fields = ["uuid",]

    def get_unit(self, id):
        return Unit.objects.get(id=id)

    def get_dates_between_two_dates(self, date1: date, date2: date):
        res = list()
        res.append(date1)
        while date1 <= date2:
            date1 += timedelta(days=1)
            res.append(date1)
        return res

    def validate(self, attrs):
        attrs = super().validate(attrs)
        start_date = attrs["start_date"]
        end_date = attrs["end_date"]
        # TODO: unhashable type: 'list'
        try:
            self.get_unit(attrs["unit"]).get_available_dates(self.get_dates_between_two_dates(start_date, end_date))
        except ValueError as e:
            raise serializers.ValidationError(e)
        return attrs
    

    @transaction.atomic
    def create(self, validated_data):
        start_date = validated_data["start_date"]
        end_date = validated_data["end_date"]
        unit = validated_data["unit"]

        for cur in self.get_dates_between_two_dates(start_date, end_date):
            ser = BookingListSerializer(data={"res_date": cur, "unit": unit})
            if ser.is_valid():
                ser.create(ser.validated_data)
            else:
                raise serializers.ValidationError(ser.errors)

        return validated_data
