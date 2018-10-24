from django.contrib import admin
from .models import Cat, PersonalCat

class CatAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')


# Register your models here.
admin.site.register(Cat, CatAdmin)
admin.site.register(PersonalCat)