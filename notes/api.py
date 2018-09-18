from rest_framework import serializers, viewsets
from .models import PersonalNote, Note

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('user_id', 'title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

class AllNotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content', 'created_at', 'last_modified')

class AllNotesViewSet(viewsets.ModelViewSet):
    serializer_class = AllNotesSerializer
    queryset = Note.objects.all()
    