from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	recipe_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.recipe_name

class Ingredient(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	ingredient_name = models.CharField(max_length=50)
	recipe_id = models.ManyToManyField(Recipe)
	def __str__(self):
		return self.ingredient_name
