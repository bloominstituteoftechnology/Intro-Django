from django.contrib import admin
from .models import Record, PrivateRecord

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'DOB', 'created_at', "last_modified")
    readonly_fields = ('created_at', 'last_modified')

admin.site.register((Record, PrivateRecord), RecordAdmin)