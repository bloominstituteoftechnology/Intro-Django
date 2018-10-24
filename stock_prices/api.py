from rest_framework import serializers, viewsets
from .models import Companies, StockPrices 


class PersonalStockSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StockPrices
        fields = ('ticker', 'closing_price')


class PersonalStockViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalStockSerializer
    queryset = StockPrices.objects.all()
