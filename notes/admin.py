from django.contrib import admin
from .models import Author, Note

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')

# Register models
admin.site.register(Author, AuthorAdmin)
admin.site.register(Note, NoteAdmin)
