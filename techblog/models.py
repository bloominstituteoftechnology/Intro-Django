from django.db import models
from uuid import uuid4

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    
