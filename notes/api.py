from rest_framework import serializers, viewsets
from .models import UserNote

class UserNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserNote
        fields = ('title', 'content')

class UserNoteViewSet(viewsets.ModelViewSet):
    serializer_class = UserNoteSerializer
    queryset = UserNote.objects.all()