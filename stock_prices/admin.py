from django.contrib import admin

# Register your models here.

from .models import Companies, PersonalCompanies

class CompaniesAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register((Companies, PersonalCompanies), CompaniesAdmin)


