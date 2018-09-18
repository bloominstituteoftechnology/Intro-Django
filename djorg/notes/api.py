from rest_framework import serializers  # for which fields
from rest_framework import viewsets  # for which rows
from .models import PersonalNote


# get our model and fields
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # what model we using
        model = PersonalNote
        # what fields should we show
        fields = ('title', 'content')

# get our rows


class PersonalNoteViewSet(viewsets.ModelViewSet):
    # ties to the class to tie to the model
    serializer_class = PersonalNoteSerializer
    # get all the objects (rows)
    queryset = PersonalNote.objects.all()
