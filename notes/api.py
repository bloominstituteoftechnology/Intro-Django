# This is a file that would use serializers and viewsets to describe which parts of the model we want to expose to the API

from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer): 

    # A nested class to tell it what parts of the model we want to access:
    class Meta: 
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace() -> Debugger 
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet): 
    # Link back to the serializer class 
    serializer_class = PersonalNoteSerializer
    # Next, add which records to search for. We could use filters here, but for now, grab all of them:
    queryset = PersonalNote.objects.none()

    def get_queryset(self): 
        user = self.request.user

        if user.is_anonymous: 
            return PersonalNote.objects.none()
        else: 
            return PersonalNote.objects.filter(user=user)

