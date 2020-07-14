from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils import timezone
# import datetime
# Create your models here.


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=timezone.now)
    # completed = models.BooleanField(default=timezone.now)
    # tags = models.CharField(max_length=30)



    # def __str__(self):
    #     return self.headline

class PersonalNote(Note):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def written_by(self):
        return self.author.user.username
