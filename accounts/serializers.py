from rest_framework import serializers
from django.db.models import Q
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    role = serializers.ChoiceField(choices=CustomUser.CHOICES, required=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'role', 'username')
        

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
        

class CustomUserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(read_only=True, allow_blank=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'token']

    
    def validate(self, data):
        email = data.get('email', None)
        passw = data.get('password', None)
        
        #check if email field is empty
        if not email:
            raise serializers.ValidationError("Please enter your email address")

        #check if email is valid
        user = CustomUser.objects.filter(
            Q(email=email)).exclude(email__isnull=True).exclude(email__iexact='').distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else: 
            raise serializers.ValidationError("The email is not valid")

        if user_obj:
            if not user_obj.check_password(passw):
                raise serializers.ValidationError("Invalid Credentials")

        #check if user is active and get or create user token
        if user_obj.is_active:
            token, created = Token.objects.get_or_create(user=user_obj)
            data['token'] = token
        else:
            raise serializers.ValidationError("User not active")

        return data
    