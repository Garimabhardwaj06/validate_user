from rest_framework import serializers
from .models import UserData
from django.contrib.auth import authenticate,login
from rest_framework import exceptions
from django.db.models import Q

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserData
        fields=['name','contact_number','email']
        # fields = '__all_'


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()
    class meta:
        model = UserData
        fields = ['usename', 'password','token',]
        extra_kwargs = {
            "password" : {"write_only": True}
        }

    def validate(self, data):
        username = data.get('username','')
        password = data['password']


        if username and password:
            # user = authenticate(username=username,password=password)
            user = UserData.objects.filter(Q(username=username))

            if user.exists():
                user_obj = user.first()

                # data['user'] = user
            else:
                error_message = 'Not a valid email'
                raise exceptions.ValidationError(error_message)

            if user_obj:
                if not user_obj.check_password(password):
                    raise exceptions.ValidationError("not a valid password")

        else:
            raise exceptions.ValidationError("one of the field is missing")

        data['token'] = ""

        return data