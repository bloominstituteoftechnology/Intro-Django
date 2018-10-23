from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    read_only = ('date_created', 'date_modified')

# Register your models here.
admin.site.register(Post, PostAdmin)

