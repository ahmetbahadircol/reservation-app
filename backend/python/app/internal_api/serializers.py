from rest_framework import serializers


class AvailavleDatesSerializer(serializers.Serializer):
    days = serializers.IntegerField()
    request_dates = serializers.DateField()
    suitable_dates = serializers.DateField()

    class Meta:
        fields = "__all__"