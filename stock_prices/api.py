from rest_framework import serializers, viewsets
from .models import Companies 


class PersonalCompaniesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Companies
        fields = ('ticker', 'closing_price')


class PersonalCompaniesViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalCompaniesSerializer
    queryset = Companies.objects.all()
