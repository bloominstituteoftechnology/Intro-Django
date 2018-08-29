from django.db import models
from uuid import uuid4

# Create your models here.

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=4, decimal_places=2)
