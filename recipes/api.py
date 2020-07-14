from rest_framework import serializers, viewsets
from .models import PersonalRecipe

class PersonalRecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalRecipe
        fields = ('name', 'description', 'steps')

    def create(self, validated_data):
        user = self.context['request'].user
        recipe = PersonalRecipe.objects.create(user=user, **validated_data)
        return recipe
    
class PersonalRecipeViewset(viewsets.ModelViewSet):
    serializer_class = PersonalRecipeSerializer
    queryset = PersonalRecipe.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalRecipe.objects.none()
        else:
            return PersonalRecipe.objects.filter(user=user)