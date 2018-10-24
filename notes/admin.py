from django.contrib import admin

# Register your models here.
from .models import Note


from .models import Dogs

from .models import PersonalNote

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')


admin.site.register(PersonalNote)
admin.site.register(Dogs)
admin.site.register(Note, NoteAdmin)
