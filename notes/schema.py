from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote

class PersonalNoteType(DjangoObjectType):

  class Meta:
    model = PersonalNote
    #Describe the data as a node in a graph for GraphQL
    interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
  """ Describe which records we want to show. """
  notes = graphene.List(PersonalNoteType)

  def resolve_notes(self, info):
    user = info.context.user # Find this with the debugger

    if user.is_anonymous:
      return PersonalNote.objects.none()
    else:
      return PersonalNote.objects.filter(user=user)
    # return PersonalNote.objects.all()

#Add a schema and attach sto the query
schema = graphene.Schema(query=Query)