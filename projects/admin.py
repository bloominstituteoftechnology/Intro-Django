from django.contrib import admin
from .models import Project, PersonalProject
class ProjectAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')
admin.site.register(Project, ProjectAdmin)
admin.site.register(PersonalProject, ProjectAdmin)
