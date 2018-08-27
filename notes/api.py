from rest_framework import serializers,viewsets

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    #inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

