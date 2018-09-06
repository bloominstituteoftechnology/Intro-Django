from django.contrib import admin
from .models import Note, PersonalNote
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_on', 'last_modified')

admin.site.register((Note,PersonalNote), NoteAdmin)