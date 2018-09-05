from graphene_django import DjangoObjectType
import graphene
from .models import PersonalTodo

class PersonalTodoType(DjangoObjectType):

    class Meta:
        model = PersonalTodo
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    personaltodos = graphene.List(PersonalTodoType)

    def resolve_todos(self, info):
        # decide which todos to return
        pass