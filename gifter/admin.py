from django.contrib import admin
from .models import Gifter, Wishlist

class GifterAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register((Gifter, Wishlist), GifterAdmin)
from django.contrib import admin

# Register your models here.
