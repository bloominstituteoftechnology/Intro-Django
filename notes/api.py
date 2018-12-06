from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    def create(self, validated_data):
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    # Link this back to the serializer class we made previously:
    queryset = PersonalNote.objects.all()
    # Next, add which records to search for.  We could use filters here, but for now, grab all of them:
    

    
