from .models import Note, PersonalNote
# The serializer and viewset libraries will describe which parts of the model we want to expose to the API.
# The viewset will visualize the model chosen by the serializer.
from rest_framework import serializers, viewsets

# Follows convention. This class will serialize the PersonalNote class/model.
class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

    # Inner (nested) class to tell it what parts of the model we want to access.
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

# The viewset visualizes the above parts of the model.
class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = Note.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)