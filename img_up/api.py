from rest_framework import serializers, viewsets
from .models import Epilepsy

class EpilepsySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Epilepsy
        fields = ('created_at', 'updated_at','numOfTotalCases','admin_name','state','numOfTotalCases','numOfChildCases','numOfAdultCases')

class EpilepsyViewSet(viewsets.ModelViewSet):
    serializer_class = EpilepsySerializer
    queryset = Epilepsy.objects.all()