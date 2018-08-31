from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote  # Table/Model to expose to from the API.
        fields = ('title', 'content')  # Select the Fields to expose.

    def create(self, validate_data):
        user = self.context['request'].user
        new_personal_note = PersonalNote.objects.create(
            user=user, **validate_data)
        return new_personal_note


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
