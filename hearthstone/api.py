from rest_framework import serializers, viewsets
from .models import UserDeck

class UserDeckSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = UserDeck
        # TODO: add more fields
        fields = ('name', 'description')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        deck = UserDeck.objects.create(user=user, **validated_data)
        return deck


class UserDeckViewSet(viewsets.ModelViewSet):
    serializer_class = UserDeckSerializer
    queryset = UserDeck.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return UserDeck.objects.none()
        else:
            return UserDeck.objects.filter(user=user)
