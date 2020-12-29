from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer, CustomUserLoginSerializer
from .models import CustomUser

# Create your views here.

class UserRegistration(generics.CreateAPIView):
    #create user
    permission_classes = (AllowAny, )
    serializer_class = CustomUserSerializer
    queryset  = CustomUser.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        role = serializer.validated_data['role']
        user.role = role
        user.save()


class UserLogin(APIView):

    permission_classes = (AllowAny, )
    serializer_class = CustomUserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            context = {
                "data" : serializer.data,
                "status" : "User logged in successfully"
            }
            return Response(context, status=status.HTTP_200_OK)

        return Response(serializer_class.data, status=status.HTTP_400_BAD_REQUEST)