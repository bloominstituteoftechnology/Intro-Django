from rest_framework import serializers, viewsets
from .models import PersonalNote, FavoriteMovies

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()


class FavoriteMoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavoriteMovies
        fields = ('title', 'year')

class FavoriteMoviesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteMoviesSerializer
    queryset = FavoriteMovies.objects.all()