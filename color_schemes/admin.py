from django.contrib import admin

from .models import ColorScheme, PersonalColorScheme

class ColorSchemeAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(ColorScheme, ColorSchemeAdmin)
admin.site.register(PersonalColorScheme, ColorSchemeAdmin)