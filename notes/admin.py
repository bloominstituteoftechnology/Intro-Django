from django.contrib import admin

from .models import Note, PersonalNote #, AccessRecord, Topic, Webpage

class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
# admin.site.register(Topic)
# admin.site.register(AccessRecord)
# admin.site.register(Webpage)
