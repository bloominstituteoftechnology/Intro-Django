from graphene_django import DjangoObjectType
import graphene
from .models import PersonalBook

class PersonalBookType(DjangoObjectType):

    class Meta:
        model = PersonalBook
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    books = graphene.List(PersonalBookType)

    def resolve_books(self, info):
        """Decide which books to return."""
        user = info.context.user

        if user.is_anonymous:
            return PersonalBook.objects.none()
        else:
            return PersonalBook.objects.filter(user=user)

schema = graphene.Schema(query=Query)