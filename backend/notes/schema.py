from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel  # <-- Right here

class PersonalNote(DjangoObjectType):
    """Describe which model we want to expose through GraphQL."""
    class Meta:
        model = PersonalNoteModel

        # Describe the data as a node in a graph for GraphQL
        interface = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    """Describe which records we want to show."""
    notes = graphene.List(PersonalNote)

    def resolve_notes(self, info):
        """Decide what notes to return."""
        user = info.context.user  # Find this with the debugger

        if user.is_anonymous:
            return PersonalNoteModel.objects.none()
        else:
            return PersonalNoteModel.objects.filter(user=user)

# Add a schema and attach to the query
schema = graphene.Schema(query=Query)