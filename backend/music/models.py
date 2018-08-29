from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from uuid import uuid4

# Create your models here.
class Music(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    title = models.CharField(max_length=200)
    composer_last_name = models.CharField(max_length=200)
    composer_first_name = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        entry = self.composer_last_name + " " + self.title
        return entry

    class Meta:
        verbose_name="music"
        verbose_name_plural="music"
        ordering = ['composer_last_name', 'title']
    
class PersonalMusic(Music):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name="personal music"
        verbose_name_plural="personal music"
        ordering = ['composer_last_name', 'title']