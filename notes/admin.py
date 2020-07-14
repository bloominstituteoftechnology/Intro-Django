from django.contrib import admin
from .models import Posts, PersonalPost

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

# Register your models here.
admin.site.register(Posts, PostAdmin)
admin.site.register(PersonalPost)