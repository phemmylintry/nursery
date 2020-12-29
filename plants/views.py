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
# Create your views here.

class PlantsCreateView(generics.CreateAPIView):
    serializer_class = PlantsSerializer
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsNurseryPermission)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class PlantsDetailView(generics.RetrieveAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (permissions.LoggedInPermission, )


class PlantsListView(generics.ListAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    permission_classes = (permissions.LoggedInPermission, )
