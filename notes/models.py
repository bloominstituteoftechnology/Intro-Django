from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Notes):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CompsciNotes(Notes):
    title2 = models.CharField(max_length=200)
    content2 = models.TextField(blank=True)