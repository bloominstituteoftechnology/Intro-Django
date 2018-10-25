from django.contrib import admin
from .models import Note, PersonalNote


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, NoteAdmin)
