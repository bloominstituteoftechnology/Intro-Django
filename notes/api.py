''' 
This is where we'll put our RESTful api 
that connects the model to the rest framework 
'''

# --> Define the fields we want to export via serializer
from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
  # --> Register model we want
  # --> Register fields we want from the model

  class Meta: # --> Holds metadata
    model = PersonalNote
    fields = ('title', 'content')
  
  def create(self, validated_data): 
    # --> Validated_data looks like {'title': 'title_stuff', 'content': 'content_stuff'}
    user = self.context['request'].user # --> Found via debugger
    note = PersonalNote.objects.create(user = user, **validated_data) # --> Pass in data as kwargs || use some more review on kwargs
    return note


class PersonalNoteViewSet(viewsets.ModelViewSet): # --> This is where we decide which records to return
  # --> Attach it to serializer we made
  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.none() # --> Retrieve none

  def get_queryset(self): # --> Looking to over-ride the queryset so we can only have notes for their own user
    user = self.request.user

    if user.is_anonymous: # --> Not logged in
      return PersonalNote.objects.none() # --> Return empty array
    else:
      return PersonalNote.objects.filter(user = user) # --> We want to filter all the notes
      # --> Its filtering based on the user that is logged in