from django.db import models
from uuid import uuid4
from django.utils import timezone
import datetime

from django.contrib.auth.models import User

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    expiration = models.DateTimeField(default=timezone.now() + datetime.timedelta(hours=36))

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)