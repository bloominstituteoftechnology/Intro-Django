from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    isComplete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalTask(Task):
    user = models.ForeignKey(User, on_delete=models.CASCADE)