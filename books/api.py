from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalBookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalBook
        fields = ('title', 'genre')

class PersonalBookViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBookSerializer
    queryset = PersonalBook.objects.all()