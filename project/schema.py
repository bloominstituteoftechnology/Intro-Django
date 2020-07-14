from django.cong import settings
from graphene.django import DjangoObjectType
import graphene
from .models import Pokemon

class PokemonType(DjangoObjectType):

    class Meta:
        model = Pokemon
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):

    Pokemons = graphene.List(PokemonType)

    def resolve_Pokemons(self, info):
        return Pokemon.objects.all

schema = graphene.Schema(query=Query)