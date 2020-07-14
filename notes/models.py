from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User




# Create your models here.
class Note(models.Model):
    id =  models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 30)
    content = models.TextField(blank=True)
    author = models.CharField(max_length = 30)
    date = models.DateField(auto_now=True)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # this should work
    # I already nuked my sql and redid the migrations 
    # very strange I thought about starting over, but don't want to
    # finding the error is better
    def __str__(self):
        return self.title

class Author(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    name = models.CharField(max_length = 33)
    # what is important about Author class? I removed a ref to it from another file
    # don't remember why
    def __str__(self):
        return self.name





