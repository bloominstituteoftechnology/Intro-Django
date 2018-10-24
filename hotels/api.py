from rest_framework import serializers, viewsets
from .models import  DifferentApartment

class DifferentApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DifferentApartment
        fields = ( 'Name', 'Phone', 'Website', 'Email', 'Address', 'Zip', 'distance')

    def create(self, validated_data):
        apartment = DifferentApartment.objects.create(**validated_data)
        # return apartment
        # import pdb; pdb.set_trace()  # Start the debugger here
        user = self.context['request'].user
        return apartment


class DifferentApartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DifferentApartmentSerializer
    queryset = DifferentApartment.objects.all()
