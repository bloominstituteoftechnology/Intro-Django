from rest_framework import serializers, viewsets
from .models import City


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ("country", "capital", "wiki", "visited")

    def create(self, validated_data):
        user = self.context["request"].user
        country = City.objects.create(user=user, **validated_data)
        return country


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return City.objects.none()

        else:
            return City.objects.filter(user=user)

