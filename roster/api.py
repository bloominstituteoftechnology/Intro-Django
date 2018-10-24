from rest_framework import serializers, viewsets
from .models import PersonalPlayer

class PersonalPlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalPlayer
        fields = ('firstName', 'lastName', 'position', 'team')

class PersonalPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalPlayerSerializer
    queryset = PersonalPlayer.objects.all()