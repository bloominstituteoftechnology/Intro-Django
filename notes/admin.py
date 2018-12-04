from django.contrib import admin
from .models import Note
from .models import PersonalNote

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')


admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)