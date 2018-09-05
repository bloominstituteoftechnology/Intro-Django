from django.db import models
from uuid import uuid4

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    def __str__(self):
        return f'<Note: {self.id} {self.title}>'  # return format string for note title
