from django.db import models
from uuid import uuid4
# Create your models here.
from django.contrib.auth.models import User

class Address(models.Model):
    friend = models.CharField(max_length=200)
    address = models.TextField(blank=False)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    logged_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
# Create your models here.
