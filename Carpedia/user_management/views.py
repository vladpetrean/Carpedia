# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

# Create your views here.
from rest_auth.views import LogoutView, django_logout, LoginView

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_auth.views import django_logout
from rest_framework.response import Response

from user_management.serializer import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LogOut(LogoutView):
    permission_classes = (AllowAny,)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
            request.session.flush()
        except (AttributeError, ObjectDoesNotExist):
            pass

        django_logout(request)

        return Response({"detail": "Successfully logged out."}, status=200)


class Login(LoginView):
    def post(self, request, *args, **kwargs):

        try:
            # make sure that the user is logged out, be fore trying to login again.
            request.user.auth_token.delete()
            request.session.flush()
            django_logout(request)
        except (AttributeError, ObjectDoesNotExist):
            pass

        # Perform login now.
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()
