from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import CustomUserSerializer, CustomUserLoginSerializer
from django.contrib.auth import get_user_model
from . import permissions
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

# Create your views here.

class UserRegistration(APIView):

    #create user
    permission_classes = (permissions.UserViewsPermissions, )
    authentication_classes = (TokenAuthentication,)
    
    @swagger_auto_schema(
        request_body = CustomUserSerializer,
        operation_description="Create a user",
    )

    def post(self, request):
        request = self.request
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            role = serializer.validated_data['role']
            user.role = role
            user.save()

            return Response (
                {
                    "status" : "User created successfully",
                    "token" : Token.objects.create(user=user).key,
                    "data" : serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(ObtainAuthToken):

    serializer_class = CustomUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request' : request})
        if serializer.is_valid(raise_exception=True):
            return Response(
                {
                    "status" : "Login successful",
                    "data" : serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)