from django.db import models
from uuid import uuid4

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    isDone = models.BooleanField(default=False)