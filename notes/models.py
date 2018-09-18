from django.db import models
from uuid import uuid4 
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) 
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=20)
    tags = models.ManyToManyField('Tag', related_name='notes')

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False) 
    tag = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)