from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Apartment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # so what do
    # cause I thought I did repeat the lines idk
    # like I thought it was just the sql request that had to change
    # you just do commands in sql and look at the results...?
    # doesn't seem anything comes out of it other than satisfying intellectual curiosity
    # when you put it that way does that mean i'm done? with that section atleast because all I think I Needed to do for this was hit some sql requests in the terminal but I wanted
    #to hit them to see. I Just was unsure of what I was trying to grab but maybe I could do like a dir or idk cause I don't know Users stuffs
    # if you can wait a few, we can do it together
    # but yeah i think you'd be done
    # that would work
    Name = models.CharField(max_length=64)
    Phone = models.IntegerField()
    Website = models.CharField(max_length=200)
    Email = models.EmailField(max_length=30)
    Address = models.CharField(max_length=200)
    Zip = models.IntegerField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    # What i'm entering to the console but it erased on me once so dind't want to risk it without typing it down
    # Name='Livable Place', Phone='3141234567', Website='LP.com', Email='LP@LP.com', Address='420 high St', Zip ='13337', distance='4.7'

class DifferentApartment(Apartment):
    user = models.ForeignKey(User, on_delete=models.CASCADE)