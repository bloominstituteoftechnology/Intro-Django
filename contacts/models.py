from django.db import models
from uuid import uuid4
# Create your models here.
class Contact(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  name = models.CharField(max_length=150)
  phone_number = models.TextField(blank=True, max_length=30)