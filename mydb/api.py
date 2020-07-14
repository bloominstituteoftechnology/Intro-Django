from rest_framework import serializers, viewsets
from .models import ShelterDog, Dog

class ShelterDogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ShelterDog
        fields = ('name',)

    def create(self, validated_data):
        city = self.context['request'].user
        pup = ShelterDog.objects.create(city = city, **validated_data)
        return pup

class ShelterDogViewSet(viewsets.ModelViewSet):
    serializer_class = ShelterDogSerializer
    queryset = ShelterDog.objects.all()

class DogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dog
        fields = ('name',)

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Dog.objects.none()
        else:
            return Dog.objects.all()
