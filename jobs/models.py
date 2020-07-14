from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    city_state = models.CharField(max_length=200)
    date_applied = models.DateField(blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalJob(Job):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
