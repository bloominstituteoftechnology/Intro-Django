from rest_framework import serializers,viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ("title","content")#'__all__'

    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    queryset = PersonalNote.objects.all()
    serializer_class = PersonalNoteSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)