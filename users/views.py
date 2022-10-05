from django.shortcuts import render

from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView,mixins,ListCreateAPIView,RetrieveUpdateDestroyAPIView


from .serializers import RegisterSerializer




class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
   


    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()  ##BU AŞAMADA TOKEN OLUŞUR...
        data=serializer.data
        token=Token.objects.get(user=user)
        data['token']=token.key
        headers=self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
