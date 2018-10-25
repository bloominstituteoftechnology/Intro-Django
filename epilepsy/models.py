from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class EpilepsyData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=200)
    # numOfDiagnoses = models.CharField(max_length=200)
    numOfDiagnoses = models.IntegerField()

class PersonalEpilepsyData(EpilepsyData):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
