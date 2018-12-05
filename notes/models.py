from django.db import models

from uuid import uuid4

# Create your models here.
class Note(models.Model):  # extends the Model class from django.db
    # unique id, not null primary key, default=uuid4 means random uuid, user cannot edit
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)  
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # see day2.md re: arguments here
    last_modified = models.DateTimeField(auto_now=True)

