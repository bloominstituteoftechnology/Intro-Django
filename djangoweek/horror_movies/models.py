from django.db import models
from uuid import uuid4
# Create your models here.

class Movies(models.Model):
    id = models.UUIDFeild(primary_key = True, editable = False, default = uuid4)
    title = models.CharFeild(Max_length = 200)
    content = models.TextFeild(blank = True)