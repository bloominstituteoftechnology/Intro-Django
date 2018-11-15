from rest_framework import serializers, viewset
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('completed')

class PersonalNoteViewSet(viewset.ModelViewSet):
    serializers_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
