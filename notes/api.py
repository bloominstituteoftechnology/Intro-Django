# import serializers and viewsets
from rest_framework import serializers, viewsets
# import PersonalNote class from models
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # inner class (nested class) to tell it what parts of the model we want to access
    class Meta:
        model = PersonalNote
        fields = ('title', 'content', 'likes_seafood')
    
    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    # add which records to search for. Currently searching for all of them
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)