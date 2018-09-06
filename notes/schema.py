from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel

class PersonalNote(DjangoObjectType):
    """ Describe which model we want to expose through GraphQL."""
    class Meta:
        model = PersonalNoteModel
        # Describe the data as a node in a graph for GraphQL
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    """ Describe which records we want to show."""
    notes = graphene.List(PersonalNote)

    def resolve_notes(self, info):
        """ Decide what notes to return."""
        user = info.context.user    # Find this with the debugger

        if  user.is_anonymous:
            return PersonalNoteModel.objects.none()
        else:
            return PersonalNoteModel.objects.filter(user=user)

class CreatePersonalNote(graphene.Mutation):

    class Arguments:
        """ input """
        title = graphene.String()
        content = graphene.String()

    """ output """
    personalnote = graphene.Field(PersonalNote)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, content):

        user = info.context.user

        if user.is_anonymous:
            return CreatePersonalNote(ok=False, status="must be logged in")
        else:
            new_note = PersonalNoteModel(title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personalnote=new_note, ok=True, status="success")


class Mutation(graphene.ObjectType):
    create_personal_note = CreatePersonalNote.Field()


# Add a schema and attach to the query
schema = graphene.Schema(query=Query, mutation=Mutation)



