from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    content = models.CharField(max_length=50)
    note_id = models.IntegerField(editable=True, null=True, blank=True)
