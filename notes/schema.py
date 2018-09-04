# from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote as PersonalNoteModel


class PersonalNote(DjangoObjectType):
    """Describe notes model you want to expose through GraphQL"""

    class Meta:
        model = PersonalNoteModel

        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    """Describe the records you want to show"""

    personalnotes = graphene.List(PersonalNote)

    def resolve_personalnotes(self, info):
        """Decide what notes to return."""
        user = info.context.user

        if user.is_anonymous:
            return PersonalNoteModel.objects.none()
        else:
            return PersonalNoteModel.objects.filter(user=user)


class CreatePersonalNote(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    personalnote = graphene.Field(PersonalNote)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, content):
        user = info.context.user

        if user.is_anonymous:
            return CreatePersonalNote(ok=False, status="Must be logged in!")
        else:
            new_note = PersonalNoteModel(title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personalnote=new_note, ok=True, status="ok")


class NotesMutation(graphene.AbstractType):
    create_personal_note = CreatePersonalNote.Field()
