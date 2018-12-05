from django.db import models
from uuid import uuid4
# Create your models here.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age =  models.IntegerField()
    zombie = models.BooleanField()

