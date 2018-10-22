from rest_framework import serializers, viewsets
from .models import PersonalPost


class PersonalPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalPost
        fields = ('title', 'content')


class PersonalPostViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalPostSerializer
    queryset = PersonalPost.objects.all()