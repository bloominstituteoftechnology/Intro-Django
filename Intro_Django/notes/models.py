from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    OCCUPATION_CHOICES = (
        ('CS', 'Computer Scientist'),
        ('FS', 'Full Stack Web Developer'),
        ('DS', 'Data Scientist'),
        ('RE', 'React Engineer'),
    )
    occupation = models.TextField(max_length=1, choices=OCCUPATION_CHOICES)

class Hobbies(Person):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    HOBBIE_CHOICES = (
        ('SP', 'Sports'),
        ('TV', 'Watching Content'),
        ('GA', 'Gardening'),
        ('TR', 'Traveling')
    )
    hobby_description = models.TextField(blank=True)

# class Language(models.Model):
#     language = models.