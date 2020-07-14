from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)