from django.db import models
from uuid import uuid4

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    author = models.TextField()



