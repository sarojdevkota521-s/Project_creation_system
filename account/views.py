from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EmailSerializer(TokenObtainPairSerializer):
    username_field = 'email'

class EmailTOkenView(TokenObtainPairView):
    serializer_class = EmailSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




