from django.db import models
from uuid import uuid4

class Note(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title      = models.CharField(max_length=255)
    author     = models.CharField(max_length=32)
    # difference btwn auto_now and auto_now_add is
    # auto_now_add is invoked once, when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed  = models.BooleanField(default=False)
    body       = models.TextField(blank=True)

class Author(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=32)
    last_name  = models.CharField(max_length=32)
    username   = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
