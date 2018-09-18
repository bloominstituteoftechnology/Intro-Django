from django.contrib import admin

from .models import Contact, PersonalContact

# Register your models here.
admin.site.register(Contact)
admin.site.register(PersonalContact)
