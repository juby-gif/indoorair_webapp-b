from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        request = self.context.get('request')

        # This is for debugging purposes only.
        print(username, password)

        try:
            user = authenticate(username=username, password=password)
            if user:
                print("PRE-LOGIN", user.get_full_name())
                login(request, user)
                print("POST-LOGIN", user.get_full_name())
                return user
        except Exception as e:
            print(e)
        raise serializers.ValidationError({
             'message': 'Could not log in, username or password are incorrect.'
        })
