from django.contrib import admin
from .models import Recipe, Ingredient

class RecipeAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
