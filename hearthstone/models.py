from django.db import models
from uuid import uuid4
# Create your models here.
class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    deck_class = models.CharField(max_length=200)
    link = URLField(max_length=500)
    description = models.TextField(blank=True)
    