from django.contrib import admin
from .models import Author, Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'written_by', 'updated_at')
    list_filter = ('updated_at', 'completed')
    readonly_fields = ('created_at', 'updated_at')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user',)

# Register models
admin.site.register(Author, AuthorAdmin)
admin.site.register(Note, NoteAdmin)
