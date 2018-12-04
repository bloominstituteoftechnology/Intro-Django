from django.contrib import admin
from .models import Note, PersonalNote
# . means look in the current directory

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'last_editted')

# Register your models here.

admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
