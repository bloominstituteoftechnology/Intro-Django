from django.contrib import admin

from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Appointment, AppointmentAdmin)

