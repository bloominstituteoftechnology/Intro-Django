from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model): # This gives our new class access to all of the built-in functionality in models.Model
  # Primary key is how the database tracks records.
  # Default calls a function to randomly generate a unique identifier.
  # We make editable false because we never want to change the key
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # serves as a unique identifier for each record
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)