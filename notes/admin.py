from django.contrib import admin
from .models import Note, NoteAdmin


# Register your models here.
admin.site.register(Note, NoteAdmin)