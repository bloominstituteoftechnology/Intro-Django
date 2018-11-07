from django.db import models

# Create your models here.
class Note(models.Model):
    id = 
    title = models.CharField(max_length = 30)
    body = models.TextField(blank = True)
    author = models.CharField()
    date = models.DateField()