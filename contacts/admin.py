from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact, PersonalContact


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')
# Register your models here.


admin.site.register(Contact, ContactAdmin)
admin.site.register(PersonalContact)
