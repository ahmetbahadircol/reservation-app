from rest_framework import serializers


class AvailableDatesSerializer(serializers.Serializer):
    days = serializers.IntegerField()
    request_dates = serializers.SerializerMethodField()
    suitable_dates = serializers.SerializerMethodField()
    class Meta:
        fields = "__all__"

    def get_request_dates(self, obj):
        breakpoint()
        return obj.start_date.strftime('%y-%m-%d') if obj.start_date else None

    def get_suitable_dates(self, obj):
        return obj.end_date.strftime('%y-%m-%d') if obj.end_date else None