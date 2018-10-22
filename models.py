from django.db import models
from uuid import uuid4

class Garment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    dscription = models.TextField(blank=True)


# Create your models here.
