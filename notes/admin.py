from django.contrib import admin


# Register your models here.
from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
	list_display = ('title', 'content')
	readonly_fields=('created_at', 'last_modified')
	list_filter=['created_at']

class PersonalNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, PersonalNoteAdmin)

