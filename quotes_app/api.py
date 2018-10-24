from rest_framework import serializers, viewsets
from models import Quote

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Quote
        fields=('author','content')
class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class=QuoteSerializer
    queryset=Quote.objects.all()