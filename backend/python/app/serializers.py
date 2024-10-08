from datetime import timedelta, date

from reservation_app.utils import now
from .models import Booking, Car, Hotel, Unit
from rest_framework import serializers
from django.db import transaction


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
        read_only_fields = [
            "uuid",
        ]


class HotelSerializer(HotelListSerializer):
    pass


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        read_only_fields = [
            "uuid",
        ]


class CarSerializer(CarListSerializer):
    pass


class BookingListSerializer(serializers.ModelSerializer):
    res_date = serializers.DateField()

    class Meta:
        model = Booking
        read_only_fields = ["uuid", "days"]
        fields = ["res_date", "unit"] + read_only_fields


class BookingSerializer(BookingListSerializer):
    pass


class MultiBookingCreateSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    unit = serializers.IntegerField()

    class Meta:
        fields = "__all__"
        read_only_fields = [
            "uuid",
        ]

    def get_unit(self, id):
        return Unit.objects.get(id=id)

    def get_dates_between_two_dates(self, date1: date, date2: date) -> list[date]:
        res = list()
        res.append(date1)
        while date1 < date2:
            date1 += timedelta(days=1)
            res.append(date1)
        return res

    def validate(self, attrs):
        attrs = super().validate(attrs)
        start_date = attrs["start_date"]
        end_date = attrs["end_date"]

        if start_date > end_date:
            raise serializers.ValidationError(
                "start_date cannot be bigger than end_date."
            )

        if start_date < now().date():
            raise serializers.ValidationError("start_date cannot be in the past.")

        if (
            len(self.get_dates_between_two_dates(start_date, end_date))
            > Booking.BOOKING_INTERVAL_DAY
        ):
            raise serializers.ValidationError(
                f"Date range cannot be longer than {Booking.BOOKING_INTERVAL_DAY} days."
            )

        unit = self.get_unit(attrs["unit"])
        try:
            unit.get_available_dates(
                tuple(self.get_dates_between_two_dates(start_date, end_date))
            )
        except ValueError as e:
            raise serializers.ValidationError(e)
        print("Succesfully fetched from GO")
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
