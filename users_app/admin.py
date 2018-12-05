from django.contrib import admin
from users_app.models import User, Note, PersonalNote


admin.site.register(User)
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')
    
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, NoteAdmin)
