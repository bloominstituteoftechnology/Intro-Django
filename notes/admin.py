from django.contrib import admin

# . means look in the current directory

from .models import Note
# Register your models here.
admin.site.register(Note)
