from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    thingy = models.CharField(max_length=200)
    adjective = models.CharField(max_length=200)
