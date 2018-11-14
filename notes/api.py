from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        note = PersonalNote.objects.create(**validated_data)
        return note
        # import pdb; pdb.set_trace()
        # pass

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()