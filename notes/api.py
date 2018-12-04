# this is where we put our restful api stuff that connects to the framework

from rest_framework import serializers, viewsets
from .models import PersonalNote

# make a serializer that helps determine which field we need to expose
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

  # Inner class nested inside PersonalNoteSerializer
  # tell it what parts of the model we want to access
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet): # this will tell us which row we are interested in showing
  # Links it back to the serializer class we made, PersonalNoteSerializer
  serializer_class = PersonalNoteSerializer
  # add which records to search for
  # for now we are searching all the records
  queryset = PersonalNote.objects.all()