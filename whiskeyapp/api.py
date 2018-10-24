from rest_framework import serializers, viewsets

from .models import PersonalWhiskey

class PersonalWhiskeySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalWhiskey
        fields = ('title', 'description', 'notes')

class PersonalWhiskeyViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalWhiskeySerializer
    queryset = PersonalWhiskey.objects.all()