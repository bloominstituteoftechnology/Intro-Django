# This file sets control over what fields should be viewable on our API
# 
# 

from rest_framework import serializers, viewsets
from .models import PersonalNote, URLS

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # Nested class, called Meta. Chooses which parts of the Meta we want to Access
        # Is it always called Meta? 
        # What does Meta mean? - self referential(arts)/denoting change of position 
    class Meta:
        model = PersonalNote
        # Chooses Fields of Records
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user

        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    # Chooses which Records to return
    queryset = PersonalNote.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()

        else:
            return personal.objects.filter(user=user)
