from django.cong import settings
from graphene.django import DjangoObjectType
import graphene
from .models import Person

class PersonType(DjangoObjectType):

    class Meta:
        model = Person
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):

    persons = graphene.List(PersonType)

    def resolve_persons(self, info):
        return Person.objects.all

schema = graphene.Schema(query=Query)