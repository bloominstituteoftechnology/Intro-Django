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


class CreatePersonalNote(graphene.Mutation):
    class Arguments:
        # Input fields
        title = graphene.String()
        content = graphene.String()

    # Output fields
    personalnote = graphene.Field(PersonalNoteType)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, content):

        user = info.context.user
        if user.is_anonymous:
            return CreatePersonalNote(ok=False, status="User must be logged in")
        else:
            new_note = PersonalNote(title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personalnote=new_note, ok=True, status="success")


class Mutation(graphene.ObjectType):
    create_personal_note = CreatePersonalNote.Field()
    ''' all other posible mutations have to be listed here down '''
    # create_whatever = CreateWahtEver.Field()


# Insert the new GraphQL-query into the Graphene-instance.
schema = graphene.Schema(query=Query, mutation=Mutation)
# schema = graphene.Schema(query=Query)
