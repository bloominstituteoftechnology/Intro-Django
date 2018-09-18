from rest_framework import serializers, viewsets
from .models import UserMovie

class UserMovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
      model = UserMovie
      fields = ('title', 'genre')

class UserMovieViewSet(viewsets.ModelViewSet):
  serializer_class = UserMovieSerializer
  queryset = UserMovie.objects.all()