from rest_framework import serializers, viewsets
from .models import Companies, PersonalCompanies


class PersonalCompaniesSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        companies = PersonalCompanies.objects.create(user=user,**validated_data)
        return companies
    class Meta:
        model = PersonalCompanies
        fields = ('ticker', 'name', 'description', 'shares_outstanding')


class PersonalCompaniesViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalCompaniesSerializer
    queryset = Companies.objects.none()

    def get_queryset(self):
        user = self.request.user
        
        if user.is_anonymous:
            return PersonalCompanies.objects.none()
        else:
            return PersonalCompanies.objects.filter(user=user)


# select * from stock_prices_companies;
# select * from stock_prices_personalcompanies;