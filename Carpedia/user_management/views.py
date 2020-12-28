# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny

from user_management.serializer import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)