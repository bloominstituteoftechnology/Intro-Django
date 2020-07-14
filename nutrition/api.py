from rest_framework import serializers, viewsets
from .models import PersonalMeal

class PersonalMealSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalMeal
        fields = ('type', 'name', 'date', 'calories', 'carbs', 'protein')
    
    def create(self, validated_data):
        user = self.context['request'].user
        meal = PersonalMeal.objects.create(user=user, **validated_data)

        return meal


class PersonalMealViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalMealSerializer
    queryset = PersonalMeal.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return self.queryset
        else:
            return PersonalMeal.objects.filter(user=user)