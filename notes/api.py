# import serializers and viewsets
from rest_framework import serializers, viewsets
# import PersonalNote class from models
from models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # inner class (nested class) to tell it what parts of the model we want to access
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    # add which records to search for. Currently searching for all of them
    queryset = PersonalNote.objects.all()