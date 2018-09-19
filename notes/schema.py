from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote


class PersonalNoteType(DjangoObjectType):
    """Describe which model we want to expose through GraphQL."""
    class Meta:
        model = PersonalNote

        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    personalnotes = graphene.List(PersonalNoteType)

    def resolve_personalnotes(self, info):
        user = info.context.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)


# Add a schema and attach to the query
schema = graphene.Schema(query=Query)
