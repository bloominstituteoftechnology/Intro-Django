from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Gifter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=200)
    birthday = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Wishlist(Gifter):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    