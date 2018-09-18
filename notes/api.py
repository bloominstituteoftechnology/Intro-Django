from rest_framework import serializers, viewsets
from .models import PersonalNote, Note

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

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
    