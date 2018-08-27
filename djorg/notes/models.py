from django.db import models
from uuid import uuid4  # To generate a random-unique identifier


class Notes (models.Model):
    # DONE: makemigrations && migrate
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
