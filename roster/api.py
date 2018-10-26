from rest_framework import serializers, viewsets
from .models import PersonalPlayer

class PersonalPlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalPlayer
        fields = ('firstName', 'lastName', 'position', 'team', 'nickName')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user

        player = PersonalPlayer.objects.create(user=user, **validated_data)

        return player

class PersonalPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalPlayerSerializer
    queryset = PersonalPlayer.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalPlayer.objects.none()

        else:
            return PersonalPlayer.objects.filter(user=user)