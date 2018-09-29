from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import UserData
from . serializers import UserDataSerializer,UserLoginSerializer
from rest_framework.authtoken.models import Token

from django.contrib.auth import login

class UserDetails(APIView):

    def get(self,request):
        userdata_object = UserData.objects.all()
        userdata_serializer  = UserDataSerializer(userdata_object,many=True)
        return Response(userdata_serializer.data)


def Hii(request):
    return HttpResponse('<h1> Hello user</h1>')



class UserLogin(APIView):

    def post(self,request,*args,**kwargs):
        serialized_data = UserLoginSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            new_data = serialized_data.data
            return Response(new_data,status = 200)
        return Response(serialized_data.errors,status=400)

        # serialized_data.is_valid(raise_exception=True)
        # validuser = serialized_data.validated_data['user']
        # login(request,validuser)
        # # token, created = Token.objects.get_or_create(user=validuser)
        # return Response({'token':token.key},status = 200)

