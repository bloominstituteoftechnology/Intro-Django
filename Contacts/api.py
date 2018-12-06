from rest_framework import serializers, viewsets
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'address')

    def create(self, validated_data):
        user = self.context['request'].user
        note = Person.objects.create(user=user, **validated_data)
        return note

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Person.objects.none()
        else:
            return Person.objects.filter(user=user)