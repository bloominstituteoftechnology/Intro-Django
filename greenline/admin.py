from django.contrib import admin
from .models import Post, UserPost

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(UserPost)
