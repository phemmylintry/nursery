from django.db import models
from django.conf import settings
from plants.models import Plants
# Create your models here.
class Orders(models.Model):

    ORDER_STATUS = (
        ('In-Progress', 'In-Progress'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled')
    )

    ordered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plants = models.CharField(max_length=255)
    time = models.DateTimeField(max_length=255, auto_now_add=True)
    order_status = models.CharField(max_length=255, choices=ORDER_STATUS, default="In-Progress")
    number_of_plants_ordered = models.IntegerField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    nursery = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.ordered_by}: ({self.time})"