from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    # Inner class nested inside PersonalNoteSerializer
    # this not arbitrary, Django look for Meta class
    # Meta class tells it what parts of the model we want to access:
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()  # Start the debugger here
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
            