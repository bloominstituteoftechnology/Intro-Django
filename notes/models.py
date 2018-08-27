from django.db import models
from uuid import uuid4


class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
