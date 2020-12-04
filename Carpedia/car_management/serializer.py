from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    manufacturer_name = serializers.CharField(max_length=256)
    model_name = serializers.CharField(max_length=256)
    release_year = serializers.IntegerField()
