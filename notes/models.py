from django.db import models
from uuid import uuid4
# Create your models here.

from django.contrib.auth.models import User


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable = False)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class CustomUser(User):
    USER_PERMISSIONS = (
        ('admin', 'admin'),
        ('paid_user', 'customer'),
        ('free_user', 'prospect')
    )
    permission = models.CharField(max_length= 10, choices=USER_PERMISSIONS)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
# class CodeChallenge(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable = False)
#     title = models.CharField(max_length = 100)
#     description = models.TextField(blank=True)
#     language = models.CharField(max_length = 50, blank=True)
#     completed = models.BooleanField(default=False)
#     pseudocode = models.TextField(blank=True)
