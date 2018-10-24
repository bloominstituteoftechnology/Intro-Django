from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note

class NoteType(DjangoObjectType):

    class Meta:
        model = Note

        interfaces = (graphene.relay.Node,)
        
        
class Query(graphene.ObjectType):

    notes = graphene.List(NoteType)

    def resolve_notes(self, info):
        return Note.objects.all()

schema = graphene.Schema(query=Query)