from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


# Create your models here.
class Epilepsy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    admin_name = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    numOfTotalCases = models.IntegerField()
    numOfChildCases = models.IntegerField()
    numOfAdultCases = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EpilepsyUserInput(Epilepsy):
    user_name = models.CharField(max_length=30)