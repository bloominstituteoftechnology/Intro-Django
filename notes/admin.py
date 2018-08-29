from django.contrib import admin

from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'last_modified', "id")
    readonly_fields=('created_at', 'last_modified')

# Register your models here.

admin.site.register((Note, PersonalNote), NoteAdmin)
#admin.site.register(PersonalNote)
