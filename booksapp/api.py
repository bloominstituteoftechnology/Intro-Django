from rest_framework import serializers, viewsets
from .models import PersonalBook

class PersonalBookSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalBook
        fields = ('title', 'author', 'description')


class PersonalBookViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBookSerializer
    queryset = PersonalBook.objects.all()
