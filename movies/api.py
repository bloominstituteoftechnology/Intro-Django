from rest_framework import serializers, viewsets
from .models import UserMovie

class UserMovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
      model = UserMovie
      fields = ('title', 'genre')

    def create(self, validated_data):
      user = self.context['request'].user
      movie = UserMovie.objects.create(user=user, **validated_data)
      return movie

class UserMovieViewSet(viewsets.ModelViewSet):
  serializer_class = UserMovieSerializer
  queryset = UserMovie.objects.none()

  def get_queryset(self):
    user = self.request.user
    if user.is_anonymous:
      return UserMovie.objects.none()
    else:
      return UserMovie.objects.filter(user=user)