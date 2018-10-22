from django.db import models
from uuid import uuid4


# Create your models here.
class Topic(models.Model):
   """A topic the user is learning about"""
   id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
   title = models.CharField(max_length=200, default='')
   text = models.CharField(max_length=200)
   

  
