from django.contrib import admin
from .models import Todo, PersonalTodo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register((Todo, PersonalTodo), TodoAdmin)
