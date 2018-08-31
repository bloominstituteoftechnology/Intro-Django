from rest_framework import serializers, viewsets
from .models import PersonalVideo
from rest_framework import permissions


class PersonalVideoSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        video = PersonalVideo.objects.create(user=user, **validated_data)
        return video

    class Meta:
        model = PersonalVideo
        fields = ("title", "lecturer", "cohort", "link", "created_at", "last_updated")


class PersonalVideoViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalVideoSerializer
    queryset = PersonalVideo.objects.none()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalVideo.objects.none()
        else:
            return PersonalVideo.objects.filter(user=user)
