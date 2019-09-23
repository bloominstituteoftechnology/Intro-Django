from django.db import models
from django_mysql.models import ListCharField
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.
class ColorScheme(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=80)
  color_list = ListCharField(blank=True, base_field=models.CharField(max_length=10), size=6, max_length=(6*11))

  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class PersonalColorScheme(ColorScheme):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  