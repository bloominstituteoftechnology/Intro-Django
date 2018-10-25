from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # tell which parts of the model we want to access
    class Meta:
        model = PersonalNote
        fields = ('title', 'content') 

    def create(self, validate_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validate_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)