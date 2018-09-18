from rest_framework import serializers, viewsets
from .models import PersonalNote, Band

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta: 
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()


class BandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Band
        fields = ('__all__')

class BandViewSet(viewsets.ModelViewSet):
    serializer_class = BandSerializer
    queryset = Band.objects.all()

