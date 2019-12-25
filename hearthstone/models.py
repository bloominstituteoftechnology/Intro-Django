from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    deck_format = models.CharField(max_length=200)
    link = models.URLField(max_length=500)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # formats it to not show ID
        return f'{self.name}, <ID:  {self.id}>'


class UserDeck(Deck):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 