from rest_framework import serializers  # for which fields
from rest_framework import viewsets  # for which rows
from .models import PersonalNote, Book


# get our model and fields
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # what model we using
        model = PersonalNote
        # what fields should we show
        fields = ('title', 'content')

    # overwrite default functionality
    def create(self, validated_data):
        user = self.context['request'].user
        """
        # default behavior
        note = PersonalNote.objects.create(**validated_data)  # ** is kwargs
        return note
        """
        note = PersonalNote.objects.create(
            user=user, **validated_data)  # ** is kwargs
        return note


class PersonalNoteViewSet(viewsets.ModelViewSet):  # get our rows
    # ties to the class to tie to the model
    serializer_class = PersonalNoteSerializer
    # get all the objects (rows)
    queryset = PersonalNote.objects.all()


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn')


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
