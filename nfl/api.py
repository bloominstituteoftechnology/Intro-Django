from rest_framework import serializers, viewsets
from .models import Team

class TeamSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Team
        fields = ('name',)

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        # user = self.context['request'].user
        team = Team.objects.create(**validated_data)
        return team

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Team.objects.none()
        else:
            return Team.objects.all()
