from django.db import models
from uuid import uuid4

# Create your models here.
class Recipe(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	recipe_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.recipe_name

class Ingredient(models.Model):
	ingredient_name = models.CharField(max_length=50)
	recipe_id = models.ManyToManyField(Recipe)
	def __str__(self):
		return self.ingredient_name
