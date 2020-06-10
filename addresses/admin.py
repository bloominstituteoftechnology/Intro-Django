from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('logged_at', 'last_modified')


admin.site.register(Address, AddressAdmin)

# Register your models here.
