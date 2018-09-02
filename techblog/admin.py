from django.contrib import admin
from .models import Post
from .models import PersonalNote

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register(Post, PostAdmin)
admin.site.register(PersonalNote)


