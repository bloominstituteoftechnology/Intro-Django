from django.db import models
from uuid import uuid4


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
