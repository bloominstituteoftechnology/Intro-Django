from django.db import models
from uuid import uuid4
# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable = False)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    permission = (
        ('admin', 'admin'),
        ('paid_user', 'customer'),
        ('free_user', 'prospect')
    )

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable = False)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank=True)