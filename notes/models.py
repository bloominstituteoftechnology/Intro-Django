from django.db import models
from uuid import uuid4

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    T_or_F = models.BooleanField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

# SuperUser Accounts:
# username: admin
# email: admin@gmail.com
# password: 123magic