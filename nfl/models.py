from django.db import models
from uuid import uuid4

class Teams(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)

class Games(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    team_1_id = models.UUIDField(primary_key=False, default=uuid4, editable=True)
    team_2_id = models.UUIDField(primary_key=False, default=uuid4, editable=True) 
    team_1_score = models.IntegerField()
    team_2_score = models.IntegerField()
