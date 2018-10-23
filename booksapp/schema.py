from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Book

class BookType(DjangoObjectType):

    class Meta:
        model = Book

        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):

    booksapp = graphene.List(BookType)

    def resolve_books(self, info):
        return Book.objects.all()

schema = graphene.Schema(query=Query)    



