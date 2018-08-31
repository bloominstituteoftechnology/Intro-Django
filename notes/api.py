from rest_framework import serializers, viewsets
from .models import PersonalNote
from rest_framework import permissions


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

    class Meta:
        model = PersonalNote
        fields = ("title", "content", "created_at", "last_updated")


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PersonalNote.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)
