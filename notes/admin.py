from django.contrib import admin

# Register your models here.
from .models import Author, Note, NoteAdmin

admin.site.register(Author)
admin.site.register(Note)
admin.site.register(NoteAdmin)



