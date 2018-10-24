from django.contrib import admin
from .models import Genre, PersonalMusic


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "last_modified")


# Register your models here.
admin.site.register(Genre, NoteAdmin)
admin.site.register(PersonalMusic)
