from rest_framework import serializers, viewsets
from .models import PersonalPlayer

class PersonalPlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalPlayer
        fields = ('firstName', 'lastName', 'position', 'team')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user

        player = PersonalPlayer.objects.create(user=user, **validated_data)
        
        return player

class PersonalPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalPlayerSerializer
    queryset = PersonalPlayer.objects.all()