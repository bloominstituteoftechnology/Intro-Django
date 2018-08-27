from rest_framework import serializers, viewsets
from .models import PersonalVideo


class PersonalVideoSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        video = PersonalVideo.objects.create(user=user, **validated_data)
        return video

    class Meta:
        model = PersonalVideo
        fields = ("title", "lecturer", "cohort", "link")


class PersonalVideoViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalVideoSerializer
    queryset = PersonalVideo.objects.all()
