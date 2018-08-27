from django.db import models

from datetime import datetime
from uuid import uuid4

# Create your models here.
class Meal(models.Model):
    id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name     = models.CharField(max_length=50)
    date     = models.DateTimeField(default=datetime.now())
    calories = models.IntegerField()
    carbs    = models.IntegerField()
    protein  = models.IntegerField()