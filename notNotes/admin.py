from django.contrib import admin
from .models import NotNote, NotNoteAdmin, PersonalNotNote

# Register your models here.
admin.site.register(NotNote, NotNoteAdmin)
admin.site.register(PersonalNotNote)