from rest_framework import serializers
from .models import Orders
from plants.models import Plants
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status

class OrderSerializer(serializers.ModelSerializer):

    ordered_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    nursery = serializers.CharField(max_length=255)
    plants = serializers.CharField(max_length=255)
    
    class Meta:
        model = Orders
        fields = "__all__"


    def validate(self, data):
        plants = data.get('plants', None)
        number_of_plants_ordered = data.get('number_of_plants_ordered', None)
        nursery = data.get('nursery', None)


        check_plants = Plants.objects.filter(added_by=nursery).filter(name=plants).count()
        if check_plants != 1:
            raise serializers.ValidationError("Plant is not available in this nursery")

        check_plants = Plants.objects.filter(added_by=nursery).filter(name=plants)
        price = check_plants[0].price
        
        total_price = number_of_plants_ordered * price

        data = {
            "plants" : plants,
            "total_price" : total_price,
            "number_of_plants_ordered" : number_of_plants_ordered,
            "nursery" : nursery
        }

        return data