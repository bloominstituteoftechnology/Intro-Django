from rest_framework import serializers, viewsets
from .models import PersonalCat

class PersonalCatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalCat
        fields = ('breed', 'facts')

class PersonalCatViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalCatSerializer