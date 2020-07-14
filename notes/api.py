from rest_framework import serializers, viewsets
from .models import PersonalNote, Band
from rest_framework.authtoken.models import Token

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta: 
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
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


class BandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Band
        fields = ('name', 'members', 'type_of_music', 'still_touring', 'pertinent_website')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class BandViewSet(viewsets.ModelViewSet):
    serializer_class = BandSerializer
    queryset = Band.objects.none()

    def get_queryset(self):
        user = self.request.user.username
        # import pdb; pdb.set_trace()
        if user == 'admin':
            return Band.objects.all()
        else:
            return Band.objects.none()

