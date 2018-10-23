from rest_framework import serializers,viewsets
from .models import PersonalFilm

class PersonalFilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalFilm
        fields = ('title', 'director', 'year')

class PersonalFilmViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalFilmSerializer
    queryset = PersonalFilm.objects.all()