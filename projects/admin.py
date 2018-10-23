from django.contrib import admin
from .models import Project
class ProjectAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')
admin.site.register(Project, ProjectAdmin)
