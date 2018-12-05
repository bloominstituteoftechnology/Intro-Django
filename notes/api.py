from rest_framework import serializers, viewsets
from .models import PersonalNote

class Meta:
     model = PersonalNote
     fields = ('title', 'content')

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
