from django.contrib import admin

# Register your models here.
from .models import Note
from .models import PersonalNote

# class NoteAdmin(admin.ModelAdmin):
# 	readonly_fields=('created_at', 'last_modified')


admin.site.register(Note)
admin.site.register(PersonalNote)