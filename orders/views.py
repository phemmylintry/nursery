from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Orders
from plants.models import Plants
from drf_yasg.utils import swagger_auto_schema
from .serializers import OrderSerializer
from accounts import permissions

class OrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsUserPermission)
    authentication_class = (TokenAuthentication, )

    @swagger_auto_schema(
        request_body=OrderSerializer,
        operation_description="Order for a plant",
    )

    def perform_create(self, serializer):
        ordered_by = self.request.user
        return serializer.save(ordered_by=ordered_by)

class OrderListView(APIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.LoggedInPermission, permissions.UserIsNurseryPermission)
    authentication_class = (TokenAuthentication, )
    
    def get(self, request):
        user = request.user.id
        orders = Orders.objects.filter(nursery=user)
        
        data = []
        
        for item in orders:
            data.append({
                "Order id" : item.id,
                "Plants Ordered" : item.plants,
                "Number of order" : item.number_of_plants_ordered,
                "Total price" : item.total_price,
                "Order by" : item.ordered_by_id,
            })

        return Response(data, status=status.HTTP_200_OK)