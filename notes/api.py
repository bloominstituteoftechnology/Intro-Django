from rest_framework import serializers, viewsets
from .models import Note, PersonalNote



class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ('title', 'content')
    
    # def create(self, validated_data):
    #     # import pdb; pdb.set_trace() ''' debugger '''
    #     note = Note.objects.create(**validated_data)
    #     return note

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = PersonalNote.objects.all()


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    
    def create(self, validated_data):
        # import pdb; pdb.set_trace() ''' debugger '''
        user = self.context['request'].user
        personal_note = PersonalNote.objects.create(user=user, **validated_data)
        return personal_note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user

        ''' if user is not logged in '''
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else: 
            return PersonalNote.objects.filter(user=user)




