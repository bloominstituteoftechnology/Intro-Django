from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    id =  models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 30)
    body = models.TextField(blank = True)
    author = models.CharField(max_length = 30)
    date = models.DateField(auto_now=True)
    completed = models.BooleanField(default = False)


