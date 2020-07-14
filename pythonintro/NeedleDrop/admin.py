from django.contrib import admin
from .models import Client, RecentList

class NDAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
# Registered so that the read-only fields will show up in the admin interface.
admin.site.register((Client, RecentList), NDAdmin)
