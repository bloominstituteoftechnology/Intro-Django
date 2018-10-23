# Connecting model to rest framework

from rest_framework import serializers, viewsets
from .models import Note, Tag

class NoteSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Note
    fields = ('title', 'content')


class NoteViewSet(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()



class TagSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Tag
    fields = ('tag_name')


class TagViewSet(viewsets.ModelViewSet):
  serializer_class = TagSerializer
  queryset = Tag.objects.all()

