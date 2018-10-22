from django.db import models
from uuid import uuid4
# Create your models here.

# Note Record
# models.Model is for inheritance, Note will inherit from models.Model import
# Add fields for Note table, plus a unique identifier
class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)



class User(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  username = models.CharField(max_length=32)
