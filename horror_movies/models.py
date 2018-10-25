from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.

class Movies(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    review = models.TextField(blank = True)
    RottenTomatoes = models.URLField(blank=True)
    url = models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalMovie(Movies):
    user = models.ForeignKey(User, on_delete= models.CASCADE)

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)