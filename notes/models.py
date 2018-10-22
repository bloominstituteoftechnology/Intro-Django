from django.db import models
from uuid import uuid4
import django.utils.timezone
# Create your models here.

# Note Record
# models.Model is for inheritance, Note will inherit from models.Model import
# Add fields for Note table, plus a unique identifier
class User(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  username = models.CharField(max_length=32)

class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  user_id = models.ForeignKey(User, default=10, on_delete=models.CASCADE)

class Tag(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  tag_name = models.CharField(max_length=50)
  note_id = models.ForeignKey(Note, on_delete=models.CASCADE)
