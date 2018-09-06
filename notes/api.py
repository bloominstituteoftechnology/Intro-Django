from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):   # inherit from the specific serializer we are using for this project

    class Meta: # Inner class nested inside PersonalNoteSerializer
        model = PersonalNote    # model
        fields = ('title', 'content')   # columns

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer   # rows
    queryset = PersonalNote.objects.all()   

