from rest_framework import serializers,viewsets
from .models import PersonalFilm

class PersonalFilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalFilm
        fields = ('title', 'director', 'year')
    
    def create(self, validated_data):
        user = self.context['request'].user
        film = PersonalFilm.objects.create(user=user, **validated_data)
        return film
    # def create(self, validated_data):
    #     import pdb; pdb.set_trace() #start the debugger
    #     pass

class PersonalFilmViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalFilmSerializer
    queryset = PersonalFilm.objects.all()