from django.db import models
from uuid import uuid4

# Create your models here.
class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=300)
    ingredients = models.TextField(blank=True)
