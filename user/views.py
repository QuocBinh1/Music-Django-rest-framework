#user/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
