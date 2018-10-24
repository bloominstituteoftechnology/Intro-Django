from rest_framework import serializers, viewsets
from .models import PersonalPlayer

class PersonalPlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalPlayer
        fields = ('firstName', 'lastName')

class PersonalPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalPlayer.objects.all()