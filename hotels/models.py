from django.db import models
from uuid import uuid4

# Create your models here.

class Apartment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    Name = models.CharField(max_length=64)
    Phone = models.IntegerField()
    Website = models.CharField(max_length=200)
    Email = models.EmailField(max_length=30)
    Address = models.CharField(max_length=200)
    Zip = models.IntegerField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    # What i'm entering to the console but it erased on me once so dind't want to risk it without typing it down
    # Name='Livable Place', Phone='3141234567', Website='LP.com', Email='LP@LP.com', Address='420 high St', Zip ='13337', distance='4.7'