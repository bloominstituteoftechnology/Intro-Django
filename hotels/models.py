from django.db import models
from uuid import uuid4

# Create your models here.

class Apartment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Name = models.CharField(max_length=64)
    Phone = models.IntegerField(max_length=11)
    Website = models.CharField(max_length=200)
    Email = models.EmailField(max_length=30)
    Address = models.CharField(max_length=200)
    Zip = models.IntegerField(max_length=5)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
