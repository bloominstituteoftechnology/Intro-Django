from django.contrib import admin
from .models import Entries, PersonalNote


class EntriesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')


# Register your models here.
admin.site.register((Entries, PersonalNote), EntriesAdmin)
