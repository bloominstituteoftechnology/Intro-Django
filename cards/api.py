from rest_framework import serializers, viewset
from models import UserCollection
from models import ColorChoice
from models import TypeChoices

class UserCollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCollection
        fields = ('name', 'color')

class UserCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = UserCollectionSerializer
    queryset = UserCollection.objects.all()