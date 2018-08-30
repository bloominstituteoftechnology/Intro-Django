from django.db import models
# Imported the uuid4 library.
from uuid import uuid4
# Imported User from django.contrib.auth.models to access built-in user functionality:
# The ability to handle multiple users and have their own personal notes. 
from django.contrib.auth.models import User

# Create your models here.
# Inherits from models.Model.
class Note(models.Model):
    # Added a Universally Unique Identifier (UUID) to serve as a key for each record.
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # Added variables "title" and "content".
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    # Added new fields to keep track of created and modified dates.
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

# A new model that inherits from the Note model/class above.
class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
