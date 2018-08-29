from rest_framework import serializers, viewsets
from .models import PersonalMusic, Music

class PersonalMusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalMusic
        fields = ('title', 'composer_last_name', 'composer_first_name', 'publisher', 'notes')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalMusic.objects.create(user=user, **validated_data)
        return note
        
class PersonalMusicViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalMusicSerializer
    queryset = Music.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalMusic.objects.none()
        elif not user:
            return PersonalMusic.objects.none

        else:
            return PersonalMusic.objects.filter(user=user)
            