from rest_framework import serializers, viewset
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewset.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    query = PersonalNote.objects.all()