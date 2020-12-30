from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core import validators
from .managers import CustomUserManager
from django.conf import settings

import jwt
from datetime import datetime, timedelta

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):

    CHOICES = (
        ('user', 'User'),
        ('nursery', 'Nursery'),
    )

    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)
    role = models.CharField(max_length=10, choices=CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('role', 'username')

    objects = CustomUserManager()

    def __str__(self):
        return self.username