from rest_framework import serializers, viewsets
from .models import PersonalCard

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
    
    def create(self, validated_data):
        user = self.context['request'].user
        # import pdb; pdb.set_trace()
        card = PersonalCard.objects.create(user=user, **validated_data)
        return card

class PersonalCardViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalCardSerializer
    queryset = PersonalCard.objects.none()

    def get_query(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalCard.objects.none()
        else:
            return PersonalCard.objects.filter(user=user)