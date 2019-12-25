from rest_framework import serializers
from rest_framework import serializers, viewsets
from notes.models import PersonalNote
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
   def create(self, validated_data):
        note = PersonalNote.objects.create(**validated_data)
        return note
   class Meta:
        model = PersonalNote
        fields = ('title', 'content')
        
class PersonalNoteViewSet(viewsets.ModelViewSet):
        serializer_class = PersonalNoteSerializer
        queryset = PersonalNote.objects.none()
def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)