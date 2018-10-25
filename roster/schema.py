from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalPlayer

class PersonalPlayerType(DjangoObjectType):
    """Describe which model we want to expose through GraphQL."""
    class Meta:
        model = PersonalPlayer

        # Describing the data as a node in a graph for GraphQL
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    '''describes which records we want to show'''
    personalplayers = graphene.List(PersonalPlayerType)

    def resolve_personalplayers(self, info):
        '''decide which players to return'''
        user = info.context.user

        if user.is_anonymous:
            return PersonalPlayer.objects.none()
        else:
            return PersonalPlayer.objects.filter(user=user)

'''add a  schema and attatch to the query'''
schema = graphene.Schema(query=Query)