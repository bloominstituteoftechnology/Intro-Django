from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note (models.Model):
    id = models.UUIDField( primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 30)
    body = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # date = models.DateTimeField(auto_now=False, auto_now_add=False)


class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
