from django.contrib import admin
from .models import NotNote, PersonalNotNote, TaskList

class NotNoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

class TaskListAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(NotNote, NotNoteAdmin)
admin.site.register(PersonalNotNote, NotNoteAdmin)
admin.site.register(TaskList, TaskListAdmin)