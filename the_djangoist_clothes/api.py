from rest_framework import serializers, viewsets
from .models import UserGarment, Garment

class UserGarmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserGarment
        fields = ('name', 'description')

    def create(self, validated_data):
        user = self.context['request'].user
        garment = UserGarment.objects.create(user=user, **validated_data)
        return garment

class UserGarmentViewSet(viewsets.ModelViewSet):
    serializer_class = UserGarmentSerializer
    queryset = UserGarment.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return UserGarment.objects.none()
        else:
            return UserGarment.objects.filter(user=user)