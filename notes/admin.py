from django.contrib import admin

from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified', 'expiration_date')

# Register your models here.
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)