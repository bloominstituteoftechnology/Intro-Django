from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # BELOW DEFINES WHICH FIELDS TO SHOW
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

# BELOW DEFINES WHICH ROWS TO SHOW
class PersonalNoteViewSet(viewsets.ModelViewSet):
    # BELOW ATTACHES ABOVE SERIALIZER CLASS (TOP)
    serializer_class = PersonalNoteSerializer
    # BELOW DEFINES WHICH DATA TO RETURN
    queryset = PersonalNote.objects.all()