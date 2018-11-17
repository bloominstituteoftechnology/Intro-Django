from rest_framework import serializers, viewsets
from .models import Note, PersonalNote
from django.contrib.auth.models import User

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalNote # should this be Note instead of PersonalNote?
        fields = ('title', 'content', 'created_at')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note
        # import pdb; pdb.set_trace()
        # pass

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user
        print(user)
        # do I have to redo migrations every time I change models.py?
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            # this makes sense to me and looks like it should work
            # maybe somewhere I need to import user?
            return PersonalNote.objects.filter(user=user)