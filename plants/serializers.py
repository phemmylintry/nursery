from rest_framework import serializers
from .models import Plants
from accounts.serializers import CustomUserSerializer
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class PlantsSerializer(serializers.ModelSerializer):

    added_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Plants
        fields = ('id', 'name', 'price', 'image', 'added_by')