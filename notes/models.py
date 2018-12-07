from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    language = models.CharField(max_length=200)
    concept = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalProject(Project):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
