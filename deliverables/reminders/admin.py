from django.contrib import admin
from .models import Reminder, PersonalReminder
# Register your models here.


class ReminderAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

class PersonalReminderAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')


admin.site.register(Reminder, ReminderAdmin)
admin.site.register(PersonalReminder, PersonalReminderAdmin)