from rest_framework import serializers, viewsets
from .models import UserGarment, Garment

    class UserGarmentSerializer(serializers.HyperlinkedModelSerializer):

        class Meta:
            model = UserGarment
            fields = ('name', 'description')

    class UserGarmentViewSet(viewsets.ModelViewSet):
        serialiser_class = UserGarmentSerializer
        queryset = UserGarment.objects.all()