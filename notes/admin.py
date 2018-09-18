from django.contrib import admin

from .models import Note, PersonalNote, Band, FunkBand


class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('date_added', 'last_modified')


# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
admin.site.register(Band)
admin.site.register(FunkBand)