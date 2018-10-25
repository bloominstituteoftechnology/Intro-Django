from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Epilepsy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_name = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    numOfTotalCases = models.PositiveSmallIntegerField()
    numOfChildCases = models.PositiveSmallIntegerField()
    numOfAdultCases = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EpilepsyUserInput(Epilepsy):
    user = models.ForeignKey(User, default=uuid.uuid4, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
