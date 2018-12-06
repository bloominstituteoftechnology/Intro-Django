from django.contrib import admin
from .models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
	readonly_fields=('name', 'address')

admin.site.register(Person) 