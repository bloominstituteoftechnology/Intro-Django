from django.db import models
from uuid import uuid4

# Create your models here.
class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    position = models.CharField(max_length=9, blank=True)
    