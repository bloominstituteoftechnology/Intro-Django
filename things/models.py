from django.db import models
from uuid import uuid4

# Create your models here.


class Thing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    thing = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
