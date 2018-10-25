from django.contrib import admin
from .models import Epilepsy
# Register your models here.
admin.site.register(Epilepsy)

class EpilepsyAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'updated_at')

# Register your models here.
admin.site.unregister(Epilepsy)
admin.site.register(Epilepsy, EpilepsyAdmin)
