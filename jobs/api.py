from rest_framework import serializers, viewsets
from .models import PersonalJob

class PersonalJobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalJob
        fields = ('job_title', 'company', 'city_state')

    def create(self, validated_data):
        user = self.context['request'].user
        job = PersonalJob.objects.create(**validated_data)
        return job

class PersonalJobViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalJobSerializer
    queryset = PersonalJob.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalJob.objects.none()
        else:
            return PersonalJob.objects.filter(user=user)