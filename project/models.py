# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from uuid import uuid4
from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    blood_type = models.CharField(max_length=2)
    about = models.TextField(blank=True)