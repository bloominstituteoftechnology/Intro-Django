from django.db import models
from uuid import uuid4

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    isComplete = models.BooleanField(default=False)

# Create your models here.
