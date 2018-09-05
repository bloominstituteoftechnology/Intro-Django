from graphene_django import DjangoObjectType
import graphene
from .models import PersonalTodo

class PersonalTodoType(DjangoObjectType):

    class Meta:
        model = PersonalTodo
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    todos = graphene.List(PersonalTodoType)

    def resolve_todos(self, info):
        # decide which todos to return
        user = info.context.user

        if user.is_anonymous:
            return PersonalTodo.objects.none()
        else:
            return PersonalTodo.objects.filter(user=user)

schema = graphene.Schema(query=Query)