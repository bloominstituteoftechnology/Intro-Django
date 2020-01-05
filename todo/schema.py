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

class CreatePersonalTodo(graphene.Mutation):

    class Arguments:
        # Input fields
        title = graphene.String()
        description = graphene.String()

    # Output fields
    personaltodo = graphene.Field(PersonalTodoType)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, description):
        
        user = info.context.user

        if user.is_anonymous:
            return CreatePersonalTodo(ok=False, status="must be logged in")
        else:
            new_todo = PersonalTodo(title=title, description=description, user=user)
            new_todo.save()
            return CreatePersonalTodo(personaltodo=new_todo, ok=True, status="success")

class Mutation(graphene.ObjectType):
    create_personal_todo = CreatePersonalTodo.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)



# class CreatePersonalTodo(graphene.Mutation):

#     class Arguments:
#         title = graphene.String()
#         description = graphene.String()

#     personaltodo = graphene.Field(PersonalTodo)
#     ok = graphene.Boolean()
#     status = graphene.String()

#     def mutate(self, info, title, description):
#         user = info.context.user

#         if user.is_anonymous:
#             return CreatePersonalTodo(ok=False, status="Must be logged in!")
#         else:
#             new_todo = PersonalTodo(title=title, description=description, user=user)
#             new_todo.save()
#             return CreatePersonalTodo(personaltodo=new_todo, ok=True, status="ok")

# class Mutation(graphene.ObjectType):
#     create_personal_todo = CreatePersonalTodo.Field()