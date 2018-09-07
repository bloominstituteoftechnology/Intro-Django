from django.contrib import admin

# Register your models here.

from .models import Section, Student, ProjectManager, StudentReport, SprintStatus, Sprint, StudentSprint

class DatesAdmin(admin.ModelAdmin):
  readonly_fields=('created_at', 'last_modified')

admin.site.register((
    Section,
    Student, 
    ProjectManager, 
    StudentReport, 
    SprintStatus, 
    Sprint,
    StudentSprint), 
  DatesAdmin)