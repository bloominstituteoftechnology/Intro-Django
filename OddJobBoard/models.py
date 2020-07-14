from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
class OddJobBoard(models.Model):
    id =  models.UUIDField(primary_key=True,default=uuid4, editable=False)
    title =  models.CharField(max_length=200)
    area = models.TextField(blank=True)
    work = models.TextField(blank=True)
    email = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(OddJobBoard):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)