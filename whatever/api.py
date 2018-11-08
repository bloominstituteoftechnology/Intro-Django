from rest_framework import serializers, viewsets
from .models import PersonalNote, Note

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        # note = PersonalNote.objects.create(**validated_data)
        # return note
        user = self.context['request'].user
        return PersonalNote.objects.create(user=user, **validated_data)

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = Note.objects.none()

    def get_queryset(self):
      user = self.request.user

      if user.is_anonymous:
          return PersonalNote.objects.none()
      else:
          return PersonalNote.objects.filter(user=user)