from rest_framework import serializers, viewsets
from projects.models import PersonalProject

class PersonalProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalProject
        fields = ('language', 'concept')
    def create(self, validated_data):
        user = self.context['request'].user
        project = PersonalProject.objects.create(user=user, **validated_data)
        return project

class PersonalProjectViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalProjectSerializer
    queryset = PersonalProject.objects.none()
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalProject.objects.none()
        else:
            return PersonalProject.objects.filter(user=user)