from django.db import models
from uuid import uuid4

# Create your models here.
class SheetMusic(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    title = models.CharField(max_length=200)
    composer_last_name = models.CharField(max_length=200)
    composer_first_name = models.CharField(max_length=200)
    instrumentation = models.CharField(max_length=200)
    notes = models.TextField(blank=True, editable=True)


    def __str__(self):
        entry = self.composer_last_name + " " + self.title
        return entry
    
    class Meta:
        ordering = ['composer_last_name']