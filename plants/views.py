from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from accounts import permissions
from accounts.models import CustomUser
from .serializers import PlantsSerializer
from .models import Plants

from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class PlantsCreateView(APIView):
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsNurseryPermission)
    authentication_classes = (TokenAuthentication,)
    serializer_class = PlantsSerializer

    @swagger_auto_schema(
        request_body=PlantsSerializer,
        operation_description="Add a plant to nursery",
    )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request' : request})
        
        if serializer.is_valid():
            #check if user already has plant in store
            name = serializer.validated_data['name']
            user = request.user
            plants = Plants.objects.filter(added_by=user).filter(name=name).count()
            
            if plants != 0:
                return Response({
                    "data" : "Plant already in store"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.validated_data['added_by'] = user
            serializer.save()
            
            return Response({
                "data" : serializer.data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantsDetailView(generics.RetrieveAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsUserPermission)



class PlantsListView(generics.ListAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsUserPermission)
