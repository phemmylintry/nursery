from django.urls import path
from . import views

urlpatterns = [
    path('add_plants/', views.PlantsCreateView.as_view(), name='add_plants'),
    path('list_plants/', views.PlantsListView.as_view(), name='list_plants'),
    path('plants_details/<int:pk>/', views.PlantsDetailView.as_view(), name='plants_details')
]