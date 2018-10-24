from django.contrib import admin
from .models import Cat

class CatAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')


# Register your models here.
admin.site.register(Cat, CatAdmin)