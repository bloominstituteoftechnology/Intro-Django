from rest_framework import serializers, viewsets
from .models import Pokemon

class PokemonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pokemon
        fields = ('blood_type')


    
class PokemonViewSet(viewsets.ModelViewSet):

    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()