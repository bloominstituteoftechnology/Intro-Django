from django.contrib import admin
from .models import Job, PersonalJob

class JobAdmin(admin.ModelAdmin):
    readonly_fields=('date_added', 'last_modified')

# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(PersonalJob)