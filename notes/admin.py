from django.contrib import admin
from .models import Note, NoteAdmin, PersonalNote
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
# Register your models here.
