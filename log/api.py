from rest_framework import serializers , viewsets
from .models import PersonalTopic

class PersonalTopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalTopic
        fields = ('title', 'text')

class PersonalTopicViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalTopicSerializer
    queryset = PersonalTopic.objects.all()
