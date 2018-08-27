from django.db import models
from uuid import uuid4
# Create your models here.
class Music(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=300)
    composer_last_name = models.CharField(max_length=200)
    composer_first_name = models.CharField(max_length=200)
    editor_last_name = models.CharField(max_length = 200)
    editor_first_name = models.CharField(max_length=200)
    instrumentation = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
