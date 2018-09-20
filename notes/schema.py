from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote

class PersonalNoteType(DjangoObjectType):
    """Describe which model we want to expose through GraphQL."""
    class Meta:
        model = PersonalNote

        # Describe the data as a node in a graph for GraphQL
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    """Describe which records we want to show."""
    personalnotes = graphene.List(PersonalNoteType)

    def resolve_personalnotes(self, info):
        """Decide what notes to return."""
        user = info.context.user  # Find this with the debugger

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)

# # Add a schema and attach to the query
# schema = graphene.Schema(query=Query)

class CreatePersonalNote(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    personalnote = graphene.Field(PersonalNoteType)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, content):
        user = info.context.user

        if user.is_anonymous:
            return CreatePersonalNote(ok=False, status="Must be logged in!")
        else:
            new_note = PersonalNote(title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personalnote=new_note, ok=True, status="ok")

class Mutation(graphene.ObjectType):
    create_personal_note = CreatePersonalNote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)