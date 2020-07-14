from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    project_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    current_stage = models.CharField(max_length=200)
    plan_board = models.URLField(blank=True)
    repo = models.URLField(blank=True)

class PersonalProject(Project):
    user = models.ForeignKey(User, on_delete=models.CASCADE)