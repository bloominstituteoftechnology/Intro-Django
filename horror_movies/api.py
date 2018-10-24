from rest_framework import serializers, viewsets
from .models import PersonalMovie

class PersonalMovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalMovie
        fields = ('title', 'content')

class PersonalMovieViewSet(viewsets.ModelViewSet):
    serializer_class= PersonalMovieSerializer
    queryset = PersonalMovie.objects.all()