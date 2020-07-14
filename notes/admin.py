from django.contrib import admin
from .models import Note, PersonalNote


# show date and time in admin system
class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')


# Register your models here.
admin.site.register((Note, PersonalNote), NoteAdmin)
