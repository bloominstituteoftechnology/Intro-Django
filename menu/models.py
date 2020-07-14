from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class PersonalMenu(Menu):
    user = models.ForeignKey(User, on_delete=models.CASCADE)