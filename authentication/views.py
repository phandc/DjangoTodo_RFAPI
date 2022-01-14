from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer



class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, ) #user has already got token. Set up credential
    def get(self, request):
        user = request.user

        serializer = RegisterSerializer(user)

        return response.Response({'user': serializer.data})
        
class RegisterAPIView(GenericAPIView):
    
    authentication_classes = [] #!if not, it will raise invalid token everytime new user register?
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password) #If the given credentials(token,etc) are valid, return a User object.

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response({"message: Try again"}, status=status.HTTP_401_UNAUTHORIZED)