from django.contrib import admin

# Register your models here.
from .models import Post, PersonalPost


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')


admin.site.register((PersonalPost, Post), PostAdmin)
