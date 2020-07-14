from django.contrib import admin
from .models import Author, Note, PersonalNote 


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')
    list_filter = ('title', 'last_updated')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')


class PersonalNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated', 'created')
    list_filter = ('title', 'last_updated', 'created')


# Register your models here.  
admin.site.register(Note, NoteAdmin)
admin.site.register(Author, AuthorAdmin )
admin.site.register(PersonalNote, PersonalNoteAdmin)
