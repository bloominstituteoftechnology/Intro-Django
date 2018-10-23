from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    position = models.CharField(max_length=9, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
class PersonalPlayer(Player):
    user = models.ForeignKey(User, on_delete=models.CASCADE)