from notes.models import Brewery, Beer
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType

class BreweryNode(DjangoObjectType):
    class Meta:
        model = Brewery
        interfaces = (Node, )

class BeerNode(DjangoObjectType):
    class Meta:
        model = Beer
        interfaces = (Node, )

class Query(ObjectType):
    brewery = Node.Field(BreweryNode)
    all_breweries = DjangoConnectionField(BreweryNode)

    beer = Node.Field(BeerNode)
    all_beers = DjangoConnectionField(BeerNode)

schema = Schema(query=Query)