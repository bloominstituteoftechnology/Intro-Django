from django.db import models
from uuid import uuid4
from decouple import config
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True)
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#class NoteAdmin(admin.ModelAdmin):
#	readonly_fields=('created_at', 'last_modified')