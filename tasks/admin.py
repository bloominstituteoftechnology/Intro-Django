from django.contrib import admin

from .models import Task, PersonalTask

admin.site.register((Task, PersonalTask))

# Register your models here.
