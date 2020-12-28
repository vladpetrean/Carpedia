# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, permissions

from car_management.models import Car
from car_management.serializer import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CarSerializer
    queryset = Car.objects.all()
