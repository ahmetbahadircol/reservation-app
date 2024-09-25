from rest_framework import serializers


class AvailableDatesSerializer(serializers.Serializer):
    days = serializers.IntegerField()
    request_dates = serializers.ListField(child=serializers.DateField())
    busy_dates = serializers.ListField(child=serializers.DateField())

    class Meta:
        fields = ["days", "request_dates", "busy_dates"]

    def get_request_dates(self, obj):
        return obj.request_dates.strftime("%y-%m-%d") if obj.request_dates else None

    def get_busy_dates(self, obj):
        return obj.busy_dates.strftime("%y-%m-%d") if obj.busy_dates else None
