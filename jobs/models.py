from django.db import models
from uuid import uuid4

# Create your models here.
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    city_state = models.CharField(max_length=200)
    date_found = models.DateField(auto_now_add=True, blank=True)
    date_applied = models.DateField(blank=True)
