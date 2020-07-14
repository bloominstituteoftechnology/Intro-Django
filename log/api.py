from rest_framework import serializers , viewsets
from .models import PersonalTopic

class PersonalTopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalTopic
        fields = ('title', 'text')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        
        topic = PersonalTopic.objects.create(user=user, **validated_data)
        
        return topic

class PersonalTopicViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalTopicSerializer
    queryset = PersonalTopic.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalTopic.objects.none()

        else:
            return PersonalTopic.objects.filter(user=user)

