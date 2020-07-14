from django.contrib import admin
from .models import Notes, PersonalNote, CompsciNotes

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register(Notes, NoteAdmin)
admin.site.register(PersonalNote)
admin.site.register(CompsciNotes)