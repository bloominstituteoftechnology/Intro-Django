from rest_framework import serializers, viewsets
from quotes_app.models import Quote

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Quote
        fields=('id','author','content')
class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class=QuoteSerializer
    queryset=Quote.objects.all()