from rest_framework import serializers, viewsets
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'age', 'zombie')

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Person.objects.none()
        else:
            return Person.objects.all()
