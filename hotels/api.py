from rest_framework import serializers, viewsets
from .models import  DifferentApartment

class DifferentApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DifferentApartment
        fields = ( 'Name', 'Phone', 'Website', 'Email', 'Address', 'Zip', 'distance')

class DifferentApartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DifferentApartmentSerializer
    queryset = DifferentApartment.objects.all()
