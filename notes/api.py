from rest_framework import serializers, viewsets
from notes.models import PersonalNote, Note

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
        model = PersonalNote
        fields = ('title', 'content')
  def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

  def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
            
class PersonalNoteViewSet(viewsets.ModelViewSet):
  serializer_class = PersonalNoteSerializer
  queryset = Note.objects.none()

  
  