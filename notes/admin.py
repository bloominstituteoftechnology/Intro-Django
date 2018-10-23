from django.contrib import admin
from .models import Note, PersonalNote
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modeified')

admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)