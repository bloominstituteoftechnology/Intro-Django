from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GroceryItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)


class Vegetable(GroceryItem):
    vegetable_name = models.CharField(max_length=100, primary_key=True)


class Fruit(GroceryItem):
    fruit_name = models.ForeignKey(User, on_delete=models.CASCADE)

