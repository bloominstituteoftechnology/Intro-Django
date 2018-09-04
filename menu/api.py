from rest_framework import serializers, viewsets
from .models import PersonalMenu


class PersonalMenuSerializer(serializers.HyperlinkedModelSerializer):
    
    # What columns we want from DB
    class Meta:
        model = PersonalMenu
        fields = ('name', 'description', 'price')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        menu = PersonalMenu.objects.create(user=user,  **validated_data)
        return menu

# what rows we want from DB
class PersonalMenuViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalMenuSerializer
    queryset = PersonalMenu.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalMenu.objects.none()
        else:
            return PersonalMenu.objects.filter(user=user)
