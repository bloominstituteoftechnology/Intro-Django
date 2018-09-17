from django.contrib import admin

from .models import Note, Band

# Register your models here.
admin.site.register(Note)
admin.site.register(Band)