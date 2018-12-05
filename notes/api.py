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
    note = PersonalNote.objects.create(**validated_data) # --> Pass in data as kwargs || use some more review on kwargs
    return note


class PersonalNoteViewSet(viewsets.ModelViewSet): # --> ?
  # --> Attach it to serializer we made
  serializer_class = PersonalNoteSerializer
  queryset = PersonalNote.objects.all() # --> Retrieve everything