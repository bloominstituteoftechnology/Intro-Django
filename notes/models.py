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

class Money(models.Model):
    EARNING_CHOICE = (
        ('steal', 's'),
        ('beg', 'b'),
        ('launder', 'l'),
        ('borrow', 'bo')
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    concept = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField()
    choices = models.CharField(('EARNING_CHOICE', 'bros', 'whateves'), max_length=50)
    amount = models.IntegerField(default=1000)