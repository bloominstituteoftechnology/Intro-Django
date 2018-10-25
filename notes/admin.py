from django.contrib import admin
from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
registry = (Note, NoteAdmin, PersonalNote)
admin.site.register(registry)
