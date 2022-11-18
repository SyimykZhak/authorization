from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from django.contrib.auth.models import User
from .serializers import *
# Create your views here.
class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersListSerializers
    permission_classes = [permissions.IsAuthenticated ]

