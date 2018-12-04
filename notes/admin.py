from django.contrib import admin
from .models import Note
from .models import PersonalNote

class NoteAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin) # --> Register the note with admin site
# admin.site.register(SomeOtherModel!) --> Same thing
admin.site.register(PersonalNote, NoteAdmin)

