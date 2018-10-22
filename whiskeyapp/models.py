from django.db import models
from uuid import uuid4

# Create your models here.
class Whiskey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
