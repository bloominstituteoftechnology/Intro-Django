from django.db import models
from uuid import uuid4

# Create your models here.
class OddJobs(models.Models):
    id = models.UUIDField(primary-key=True,default=uuid4,editable=False)
    title = models.CharField(max_length=200)
    listing = models.TextField(blank=True)
    area = models.TextField(blank=True)
    email = models.TextField(blank=True)