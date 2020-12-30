from django.urls import path
from . import views

urlpatterns = [
    path('plant_order/', views.OrderView.as_view(), name='plant_order'),
    path('list_orders/', views.OrderListView.as_view(), name="list)orders")
]