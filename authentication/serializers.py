from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['username','email', 'password'] #which fields are displaued in backend


    def create(self, validated_data):
        print("Validated data", validated_data)
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    class Meta:
        model = User

        fields = ['email', 'password', 'username', 'token'] #which fields are displaued in backend

        read_only_fields = ['token']