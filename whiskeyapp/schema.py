from django.conf import settings
from graphene_django import DjangoObjectType
import graphene

from .models import Whiskey

class WhiskeyType(DjangoObjectType):
    
    class Meta:
        model = Whiskey
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):

    whiskeys = graphene.List(WhiskeyType)

    def resolve_whiskeys(self, info):
        return Whiskey.objects.all()

schema = graphene.Schema(query=Query)