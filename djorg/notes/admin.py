from django.contrib import admin

from .models import Note, PersonalNote
from .models import Book, Illustrate


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')


# class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ['year_published']


# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
admin.site.register(Book)
# admin.site.register(Book, BookAdmin)
admin.site.register(Illustrate)
