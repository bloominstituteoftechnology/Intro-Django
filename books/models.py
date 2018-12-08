from django.db import models
from uuid import uuid4

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200, blank=False, editable=True)
    author = models.CharField(max_length=200, blank=False, editable=True)