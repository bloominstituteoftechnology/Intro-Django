from django.db import models
from uuid import uuid4

# Create your models here.
class Notes(models.Model):
 title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
