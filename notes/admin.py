from django.contrib import admin
from .models import Author, Note, PersonalNote 


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'written_by', 'last_updated')
    list_filter = ('last_updated', 'completed', )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob')


class PersonalNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'written_by', 'last_updated')
    list_filter = ('last_updated', 'completed', )


# Register your models here.  
admin.site.register(Note)
admin.site.register(Author)
admin.site.register(PersonalNote)
