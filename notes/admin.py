from django.contrib import admin

from .models import Note

class NoteAdmin(admin.ModelAdmin): # To get the read-only fields to show up in the interface
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin) # register the Note model with the admin site 