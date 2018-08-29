from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalCardSerializer(serializers.HyperlinkedModelSerializer):

        # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalCard
        fields = (
        'name', 
        'cost', 
        'color', 
        'cmc', 
        'cardType', 
        'subType', 
        'cardSet', 
        'text',
        'created_at',
        'last_modified'
        )

    class PersonalCardViewSet(viewsets.ModelViewSet):
        serializer_class = PersonalCardSerializer
        queryset = PersonalCard.objects.none()

        def get_query(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalCard.objects.none()
        else:
            return PersonalCard.objects.filter(user=user)