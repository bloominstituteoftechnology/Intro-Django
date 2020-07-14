from django.contrib import admin
from .models import Author, Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'updated_at')
    list_filter = ('updated_at',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user',)

class PersonalNoteAdmin(admin.ModelAdmin):
    list_display = ('written_by', 'created_at')
    list_filter = ('author__user', 'created_at')

# Register models
admin.site.register(Author, AuthorAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, PersonalNoteAdmin)
