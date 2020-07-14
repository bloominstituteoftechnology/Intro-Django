from rest_framework import serializers, viewsets
from .models import PersonalMusic


class PersonalMusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalMusic
        fields = ("title", "content")

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context["request"].user
        music_note = PersonalMusic.objects.create(user=user, **validated_data)
        return music_note


class PersonalMusicViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalMusicSerializer
    queryset = PersonalMusic.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalMusic.objects.none()

        else:
            return PersonalMusic.objects.filter(user=user)
