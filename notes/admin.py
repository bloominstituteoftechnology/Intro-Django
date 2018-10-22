from django.contrib import admin
from .models import Notes, PersonalNote

class NotesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

# Register your models here.
admin.site.register(Notes, NotesAdmin)
admin.site.register(PersonalNote)