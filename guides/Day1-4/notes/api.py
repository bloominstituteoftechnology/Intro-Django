# This is a file that would use serializers and viewsets to describe which parts of the model we want to expose to the API

from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperLinkedModelSerializer): 

    # A nested class to tell it what parts of the model we want to access:
    class Meta: 
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet): 
    # Link back to the serializer class 
    serializer_class = PersonalNoteSerializer
    # Next, add which records to search for. We could use filters here, but for now, grab all of them:
    querset = PeronsalNote.objects.all()

