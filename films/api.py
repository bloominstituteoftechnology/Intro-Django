from rest_framework import serializers,viewsets
from .models import PersonalFilm, Film

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
    queryset = Film.objects.none()
    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalFilm.objects.none()
        else:
            return PersonalFilm.objects.filter(user=user)