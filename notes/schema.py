from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote

# Wire the model with GraphQL -> transfor the model into a GraphQL-model


class PersonalNoteType(DjangoObjectType):
    class Meta:
        model = PersonalNote

        # type of graph entity
        interfaces = (graphene.relay.Node,)


# Wire the GraphQL-model with GraphQl-qyeries
class Query(graphene.ObjectType):
    # define the data type to be returned
    # In this case is a 'list' of notes
    notes = graphene.List(PersonalNoteType)

    def resolve_notes(self, info):
        """ Decide which notes to return """
        user = info.context.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)


# Insert the new GraphQL-query into the Graphene-instance.
schema = graphene.Schema(query=Query)
