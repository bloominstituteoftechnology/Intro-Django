from django.db import models
from uuid import uuid4

# Create your models here.
class Cat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    breed = models.CharField(max_length=200)
    facts = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)