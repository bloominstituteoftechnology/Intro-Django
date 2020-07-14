from django.contrib import admin

from .models import Menu, PersonalMenu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', "id")
    readonly_fields=('created_at', 'last_modified')

# Register your models here.

admin.site.register((Menu, PersonalMenu), MenuAdmin)
