# this file uses serializers and viewsets 
# to describe which parts of the model we want to expose to the API

from rest_framework import serializers, viewsets
from .models import Note, PersonalNote

# Name the serializer class after what it is serializing.
# It will inherit from the specific serializer we are using for this project:
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # Make an inner class aka Meta to tell the serializer what parts of the model we want to access
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):  # override default .create functionality
        user = self.context['request'].user
        # import pdb; pdb.set_trace()
        # user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data) # uses kwarg
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):  # tells which rows to show
    # link to the serializer class:
    serializer_class = PersonalNoteSerializer
    # specify which records to search for:
    queryset = Note.objects.all()  # create the variable with an empty dictionary of the correct type
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)