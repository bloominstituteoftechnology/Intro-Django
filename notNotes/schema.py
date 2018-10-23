from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import NotNote

class NotNoteType(DjangoObjectType):

    class Meta:
        model = NotNote

        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):

    notNotes = graphene.List(NotNoteType)

    def resolve_notNotes(self, info):
        return NotNote.objects.all()

schema = graphene.Schema(query=Query)