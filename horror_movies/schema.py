from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from models import Movies

class MovieType(DjangoObjectType):
    class Meta:
        model = Movies
        interfaces = (graphene.relay.Node,)
class Query(graphene.ObjectType):
    horror_movies = graphene.List(MovieType)
    def resolve_movies(self, info):
        return Movies.objects.all()

schema = graphene.Schema(query=Query)

