from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# from django.utils import timezone

# Create your models here.


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # completed = models.BooleanField(default=timezone.now)

    def written_by(self):
        return self.author.user.username


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
