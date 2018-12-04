from uuid import uuid4
from django.db import models

# Create your models here.


class User(models.Model):

#    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)

# class PersonalUser(User):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
