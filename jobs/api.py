from rest_framework import serializers, viewsets
from .models import PersonalJob

class PersonalJobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalJob
        fields = ('job_title', 'company', 'city_state')

class PersonalJobViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalJobSerializer
    queryset = PersonalJob.objects.all()