from rest_framework import serializers, viewsets
from .models import PersonalNote, Hobbies

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

class HobbiesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hobbies
        fields = ('HOBBIE_CHOICES', 'hobby_description')

class HobbiesViewSet(viewsets.ModelViewSet):
    serializer_class = HobbiesSerializer
    queryset = Hobbies.objects.all()