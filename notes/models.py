from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note): #Inherits from Note
    # Creates a foreign key to create a reference to data on another table
    user = models.ForeignKey(User, on_delete=models.CASCADE)
