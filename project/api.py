from rest_framework import serializers, viewsets
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Person
        fields = ('blood_type')

    
class PersonViewSet(viewsets.ModelViewSet):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()