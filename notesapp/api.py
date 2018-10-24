# Connecting model to rest framework

from rest_framework import serializers, viewsets
from .models import Note, PersonalNote, Tag

class NoteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Note
    fields = ('title', 'content')

class NoteViewSet(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()



class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PersonalNote
    fields = ('title', 'content', 'private_content')

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


class TagSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Tag
    fields = ('tag_name',)

class TagViewSet(viewsets.ModelViewSet):
  serializer_class = TagSerializer
  queryset = Tag.objects.all()
