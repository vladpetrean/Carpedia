# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from car_management.models import Car

admin.register(User)
admin.register(Car)
