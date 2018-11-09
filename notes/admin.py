from django.contrib import admin


# Register your models here.
from .models import Author, Note

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')


admin.site.register(Author)
admin.site.register(Note)
admin.site.register(NoteAdmin)



