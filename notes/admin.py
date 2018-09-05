from django.contrib import admin
<<<<<<< HEAD
from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register((Note, PersonalNote), NoteAdmin)
=======

# Register your models here.
>>>>>>> c9ce7017b6150d6141679a2e39104dfabc7a1651
