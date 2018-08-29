from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User 

class Note(models.Model): 
    # Create your models here.
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return f'<{self.__class__.__name__}: {self.id} {self.title}>'

class PersonalNote(Note): # Inherits from Note! 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return f'<{self.__class__.__name__}: {self.id} {self.title}>'
