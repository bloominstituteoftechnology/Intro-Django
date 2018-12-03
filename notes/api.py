from rest_framework import serializers, viewsets
from .models import PersonalNote

serializer_class = PersonalNoteSerializer
queryset = PersonalNote.objects.all()

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
     # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')