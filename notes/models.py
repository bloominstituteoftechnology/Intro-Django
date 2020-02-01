from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
