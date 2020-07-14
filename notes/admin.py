from django.contrib import admin
from .models import Note, PersonalNote


# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'last_modified', "id")
    readonly_fields = ('created_at', 'last_modified')

admin.site.register((Note, PersonalNote), NoteAdmin)


