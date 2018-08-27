from django.db import models
from uuid import uuid4

# Create your models here.


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    lecturer = models.CharField(max_length=200)
    cohort = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
