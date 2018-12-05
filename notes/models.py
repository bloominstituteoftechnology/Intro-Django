from django.db import models
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

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
    choices = models.CharField(EARNING_CHOICE, max_length=50)
    amount = models.IntegerField(default=1000)