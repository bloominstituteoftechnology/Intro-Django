from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class Smurf(models.Model): # This gives our new class access to all of the built-in functionality in models.Model
  # Primary key is how the database tracks records.
  # Default calls a function to randomly generate a unique identifier.
  # We make editable false because we never want to change the key
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False) # serves as a unique identifier for each record
  name = models.CharField(max_length=200)
  age = models.CharField(max_length=200)
  size = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True) # track created dates, auto_now_add only sets create
  last_modified = models.DateTimeField(auto_now=True) # track modified dates, auto_now sets both create and update

class UsersSmurf(Smurf): # subclass that inherits all the fields in Smurf
  user = models.ForeignKey(User, on_delete=models.CASCADE)

