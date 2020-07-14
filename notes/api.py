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

    def create(self, validated_data): # overrides the default creates functionality
      # import pdb; pdb.set_trace()  # Start the debugger here

      user = self.context['request'].user
      # make a new persoinal note with the validated_data
      note = PersonalNote.objects.create(user=user, **validated_data)
        # return the note
      return note

class PersonalNoteViewSet(viewsets.ModelViewSet): # this will tell us which row we are interested in showing
  # Links it back to the serializer class we made, PersonalNoteSerializer
  serializer_class = PersonalNoteSerializer
  # add which records to search for
  # for now we are searching all the records
  queryset = PersonalNote.objects.all()

  # overrides queryset to be more specific
  # has access to the request directly, so it can be found with self.request.user
  def get_queryset(self): 
    user = self.request.user

    # If user.is_anonymous
    if user.is_anonymous:
      # return an empty dictionary of notes
      return PersonalNote.objects.none()
    else:
      # use a filter to return only the correct ones with Note.objects.filter(user=user)
      return PersonalNote.objects.filter(user=user)