# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Note, PersonalNote, Personal_Tags


class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')
	list_display = ('title',)

admin.site.register(Note)
admin.site.register(PersonalNote)
admin.site.register(Personal_Tags)
