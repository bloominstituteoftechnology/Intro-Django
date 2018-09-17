from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Movie(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=20)
  genre = models.TextField(max_length=15)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class UserMovie(Movie):
  user = models.ForeignKey(User, on_delete=models.CASCADE)