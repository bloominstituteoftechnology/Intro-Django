from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class NotNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200, default="default title")
    subtitle = models.CharField(max_length=200, default="default subtitle")
    content = models.TextField(blank=True)
    extraContent = models.TextField(blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNotNote(NotNote): #Inherits from NotNote!
    user = models.ForeignKey(User, on_delete=models.CASCADE)