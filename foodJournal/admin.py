from django.contrib import admin
from .models import Meal

class MealAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Meal, MealAdmin)


