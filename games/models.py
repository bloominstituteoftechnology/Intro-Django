from django.db import models
from uuid import uuid4

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    release_date = models.IntegerField(max_length=4)
