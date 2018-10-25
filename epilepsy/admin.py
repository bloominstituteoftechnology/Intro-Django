from django.contrib import admin
from epilepsy.models import EpilepsyData, PersonalEpilepsyData
# Register your models here.

class EpilepsyAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register((EpilepsyData, PersonalEpilepsyData), EpilepsyAdmin)
# admin.site.register(EpilepsyData)