from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model): # --> Inherit from models.Model
  id = models.UUIDField(primary_key = True, default = uuid4, editable = False) 
  # --> Primary id || always unique and searchable || 
  # --> uuid4 will generate a super long string for it
  # --> not editable
  title = models.CharField(max_length = 200)
  content = models.TextField(blank = True) # --> Kind of like a text input field || allow field to be blank

  # Day 2: Migrations with New Fields
  created_at = models.DateTimeField(auto_now_add=True) # --> Only sets on create
  last_modified = models.DateTimeField(auto_now=True) # --> Set on both create and update

class PersonalNote(Note):   # Inherits from Note!
  user = models.ForeignKey(User, on_delete=models.CASCADE) # --> Ask questions about this one