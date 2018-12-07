from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
	readonly_fields=('date_added',)

admin.site.register(Entry,EntryAdmin)

