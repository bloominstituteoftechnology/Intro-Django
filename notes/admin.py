# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote)
