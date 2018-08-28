from django.db import models
from uuid import uuid4

# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    entry = models.CharField(max_length=200)
    blog_post = models.TextField(blank=True)
