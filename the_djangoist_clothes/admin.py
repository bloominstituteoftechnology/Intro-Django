from django.contrib import admin
from .models import Garment

class GarmentAdmin(admin.ModelAdmin):
	readonly_fields=("created_at", "last_modified")

# Register your models here.
admin.site.register(Garment, GarmentAdmin)
