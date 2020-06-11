from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)