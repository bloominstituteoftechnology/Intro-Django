from django.contrib import admin

# Register your models here.
from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_on', 'last_modified')


admin.site.register((Note, PersonalNote),NoteAdmin)
