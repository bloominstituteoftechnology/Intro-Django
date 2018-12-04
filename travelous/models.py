from django.db import models
from uuid import uuid4

# Create your models here.
class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    country = models.CharField(max_length=200)
    capital = models.TextField(blank=True)
    wiki = models.URLField()
    visited = models.BooleanField(default=False)
