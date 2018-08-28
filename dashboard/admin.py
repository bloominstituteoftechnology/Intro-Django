from django.contrib import admin

# Register your models here.

from .models import StudentReport, Sprint

admin.site.register(StudentReport)
admin.site.register(Sprint)
