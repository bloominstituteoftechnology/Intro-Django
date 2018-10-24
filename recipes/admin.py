from django.contrib import admin
from .models import Recipe, PersonalRecipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(PersonalRecipe)
