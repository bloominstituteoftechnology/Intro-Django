from django.db import models
from uuid import uuid4

# TODO: Note class

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return F"Title: {self.title}, Content: {self.content}"