from django.contrib import admin


# Register your models here.
from .models import Author, Note, PersonalNote

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')
	list_filter=('created_at')


admin.site.register(Author)
admin.site.register(Note, NoteAdmin)


