from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Orders
from plants.models import Plants

from .serializers import OrderSerializer
from accounts import permissions


class OrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsUserPermission)
    authentication_class = (TokenAuthentication, )

    def perform_create(self, serializer):
        ordered_by = self.request.user
        return serializer.save(ordered_by=ordered_by)


class OrderListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsNurseryPermission)
    authentication_class = (TokenAuthentication, )