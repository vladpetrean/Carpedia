# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from car_management.models import Car
from car_management.serializer import CarSerializer


# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world")


class CarViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CarSerializer
    queryset = Car.objects.all()
