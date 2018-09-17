from django.db import models
from uuid import uuid4

# Create your models here.
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid4, editable=False)
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    tag = models.ForeignKey(Tag, default=None, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
