from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    country = models.CharField(max_length=200)
    capital = models.TextField(blank=True)
    wiki = models.URLField()
    visited = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class City(Country):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
