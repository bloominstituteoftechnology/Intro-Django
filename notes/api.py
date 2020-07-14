from rest_framework import serializers, viewsets
from .models import PersonalNote, FavoriteMovies, Brewery, Beer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)


class FavoriteMoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavoriteMovies
        fields = ('title', 'year', 'imdb_link')

    def create(self, validated_data):
        import pdb; pdb.set_trace()
        movie = FavoriteMovies.objects.create(**validated_data)
        return movie

class FavoriteMoviesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteMoviesSerializer
    queryset = FavoriteMovies.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return FavoriteMovies.objects.none()
        elif user.is_superuser:
            return FavoriteMovies.objects.all()
        else:
            return FavoriteMovies.objects.filter(user=user)


class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brewery
        fields = ('name', 'address', 'website')

    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user
        brewery = Brewery.objects.create(user=user, **validated_data)
        return brewery


class BreweryViewSet(viewsets.ModelViewSet):
    serializer_class = BrewerySerializer
    queryset = Brewery.objects.all()


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'brewery', 'abv', 'ibu')

    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user
        beer = Beer.objects.create(user=user, **validated_data)
        return beer


class BeerViewSet(viewsets.ModelViewSet):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()


class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)