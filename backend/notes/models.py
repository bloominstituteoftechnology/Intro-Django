from django.db import models
from uuid import uuid4

# Create your models here.

class Note(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(default='title', max_length=140)
    content = models.CharField(default='content', max_length=512)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    