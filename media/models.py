from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator

class Reviewer(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #models.OneToOne
    dob = models.DateField(auto_now=False, blank=True)
    def reviewed_by(self) :
        return self.reviewer.user.user
    
class Media(models.Model):
    type = models.CharField(max_length = 50, blank=True)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE) 
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 50)
    artist = models.CharField(max_length = 50)
    year_pub = models.IntegerField(default=2018)    
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=3,
            validators=[MaxValueValidator(5),
            MinValueValidator(0)])

class Book(Media):
    format = models.CharField(max_length = 50, default="Hardcover Book")

class Music(Media):
    format = models.CharField(max_length = 50, default="MP3")    
    

class Movie(Media):
    format = models.CharField(max_length = 50, default="Blu-ray")     