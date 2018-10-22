from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Note(models.Model):
    content = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
