from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

User = get_user_model()

class Plants(models.Model):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='nursery', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name