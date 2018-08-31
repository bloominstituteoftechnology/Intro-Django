from django.db import models
from uuid import uuid4  # To generate a random-unique identifier
from django.contrib.auth.models import User


class Note (models.Model):
    # DONE: makemigrations && migrate
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
