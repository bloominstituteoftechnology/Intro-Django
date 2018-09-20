from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote

class PersonalNoteType(DjangoObjectType):

    class Meta:
        model = PersonalNote
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    notes = graphene.List(PersonalNoteType)

    def resolve_notes(self, info):
        #TODO ONLY RETURN NOTES FOR USER THAT IS LOGGED IN
        return PersonalNote.objects.all()

schema = graphene.Schema(query=Query)