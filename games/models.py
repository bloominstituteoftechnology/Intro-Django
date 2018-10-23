from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from uuid import uuid4

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    release_date = models.IntegerField(
        validators=[
            MaxValueValidator(2020),
            MinValueValidator(1900)
        ], editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)   
