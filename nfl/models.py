from django.db import models
from uuid import uuid4

class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    team_1_id = models.UUIDField(primary_key=False, default=uuid4, editable=True)
    team_2_id = models.UUIDField(primary_key=False, default=uuid4, editable=True) 
    team_1_score = models.IntegerField()
    team_2_score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
