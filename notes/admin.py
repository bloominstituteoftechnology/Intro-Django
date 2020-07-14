from django.contrib import admin
from .models import Note, PersonalNote

# Will show date and time on the admin app
class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register((Note, PersonalNote), NoteAdmin)

