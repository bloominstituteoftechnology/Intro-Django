from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4

class Author(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user       = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # first_name = models.CharField(max_length=32)
    # last_name  = models.CharField(max_length=32)
    # username   = models.CharField(max_length=32)

class Note(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title      = models.CharField(max_length=255)
    author     = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body       = models.TextField(blank=True)


class PersonalNote(Note):
    completed  = models.BooleanField(default=False)

    def written_by(self):
        return self.author.user.username
