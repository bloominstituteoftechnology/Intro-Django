from rest_framework import serializers, viewsets
from .models import PersonalNotNote

class PerNotNoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        notNote = PersonalNotNote.objects.create(user=user,**validated_data)
        return notNote

    class Meta:
        model = PersonalNotNote
        fields = ('title', 'subtitle', 'content', 'extraContent')


class PerNotNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PerNotNoteSerializer
    queryset = PersonalNotNote.objects.none()

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        #THIS IS A DEBUGGER TOOL ^^

        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return PersonalNotNote.objects.none()
        else:
            return PersonalNotNote.objects.filter(user=logged_in_user)