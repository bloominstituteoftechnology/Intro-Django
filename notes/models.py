from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User
from django.utils import timezone
import datetime

def get_exp():
  return timezone.now() + datetime.timedelta(weeks=52)

# Create your models here.
class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  tags = models.CharField(blank=True, max_length=400)
  topic = models.CharField(blank=True, max_length=50)

  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  expiration_date = models.DateField(default= get_exp(), editable=False)

class PersonalNote(Note):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  