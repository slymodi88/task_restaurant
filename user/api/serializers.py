import jwt
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from resturant_task import settings
from user.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'employee_number', 'password', 'token')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        user_created_token = User.objects.create_token(user)
        return user_created_token


class UserLoginSerializer(serializers.ModelSerializer):
    employee_number = serializers.CharField(max_length=4, min_length=4)
    password = serializers.CharField(max_length=128, required=True, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    name = serializers.CharField(max_length=255,required=False)

    class Meta:
        model = User
        fields = ('id', 'name', 'employee_number', 'password', 'token')
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        employee_number = data.get("employee_number", None)
        password = data.get("password")

        user = authenticate(employee_number=employee_number, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this employee number and password is not found.'
            )
        return user
