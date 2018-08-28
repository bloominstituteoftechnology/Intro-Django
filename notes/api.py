from rest_framework import serializers, viewsets
from .models import UserNote

class UserNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserNote
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        note = UserNote.objects.create(user=user, **validated_data)
        return note

class UserNoteViewSet(viewsets.ModelViewSet):
    serializer_class = UserNoteSerializer
    queryset = UserNote.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return UserNote.objects.none()
        else:
            return UserNote.objects.filter(user=user)