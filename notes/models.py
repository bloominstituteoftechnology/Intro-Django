# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4


# admin note
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Personal_Tags(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=150)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)


# Inherits from Note! per user
class PersonalNote(Note):   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ptag = models.ForeignKey(Personal_Tags, on_delete=models.CASCADE)



    

