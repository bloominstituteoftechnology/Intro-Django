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
        user = info.context.user
        
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)

schema = graphene.Schema(query=Query)
        