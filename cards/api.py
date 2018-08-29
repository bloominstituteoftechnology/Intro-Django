from rest_framework import serializers, viewsets
from .models import UserCollection
from .models import ColorChoice
from .models import TypeChoice

class UserCollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCollection
        fields = (
            'name',
            'cost',
            'cmc',
            'color',
            'cardType',
            'subType',
            'cardSet',
            'text'
        )
    
    def create(self, validated_data):
        user = self.context['request'].user
        note = UserCollection.objects.create(user=user, **validated_data)
        return note

class UserCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = UserCollectionSerializer
    queryset = UserCollection.objects.all()