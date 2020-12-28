from rest_framework import serializers
from car_management.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('manufacturer_name', 'model_name', 'release_year')
