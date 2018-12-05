from rest_framework import serializers, viewsets
from .models import Recipe, Ingredient

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:	# Inner class nested inside RecipeSerializer
		model = Recipe
		fields = ['recipe_name']
	def create(self, validated_data):
		user = self.context['request'].user
		note = Recipe.objects.create(user=user, **validated_data)
		return note

class RecipeViewSet(viewsets.ModelViewSet):
	serializer_class = RecipeSerializer
	queryset = Recipe.objects.none()
	def get_queryset(self):
		user = self.request.user
		if user.is_anonymous:
			return Recipe.objects.none()
		else:
			return Recipe.objects.filter(user=user)


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:	# Inner class nested inside IngredientSerializer
		model = Ingredient
		fields = ['ingredient_name']
	def create(self, validated_data):
		user = self.context['request'].user
		ingredient = Ingredient.objects.create(user=user, **validated_data)
		return ingredient

class IngredientViewSet(viewsets.ModelViewSet):
	serializer_class = IngredientSerializer
	queryset = Ingredient.objects.all()