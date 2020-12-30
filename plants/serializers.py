from rest_framework import serializers
from .models import Plants
from accounts.serializers import CustomUserSerializer
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from .models import Plants

User = get_user_model()

class PlantsSerializer(serializers.ModelSerializer):

    added_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    image = serializers.ImageField()
    class Meta:
        model = Plants
        fields = ('id', 'name', 'price', 'image', 'added_by')
    
    
    # def validate(self, data):
    #     name = data.get('name', None)
    #     price = data.get('price', None)
    #     image = data.get('image', None)
        
    #     #check if user already has plants in store
    #     check_name = Plants.objects.all().filter(added_by=name)
    #     if check_name:
    #         raise serializers.ValidationError("You already have {} in your store".format(name))

    #     data = {
    #         "name" : name,
    #         "price" : price,
    #         "image" : image
    #     }

    #     return data