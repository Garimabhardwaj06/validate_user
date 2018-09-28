from django.shortcuts import render
from .models import UserData, ViewUser

from django.http import Http404

from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ValidUserDetail(APIView):
    def get_object(self, pk):
        try:
            return UserData.objects.get(pk=pk)
        except UserData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        data = ViewUser(request.POST)

        if data.is_valid():
            username = data.cleaned_data['username']
    else:
        data = ViewUser()

    # return render(request, '<name>.html', {"username": username})

