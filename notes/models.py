from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    on_dvd = models.BooleanField(default=True)
    imdb_link = models.URLField(default='http://www.imdb.com')
    created_at = models.DateTimeField(auto_now_add=True)

class FavoriteMovies(Movie):
    user = models.ForeignKey(User, on_delete=models.CASCADE)