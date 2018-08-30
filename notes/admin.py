from django.contrib import admin
from .models import Note, PersonalNote
class NoteAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified')


admin.site.register((Note, PersonalNote),NoteAdmin)
# admin.site.register(PersonalNote)

# Register your models here.