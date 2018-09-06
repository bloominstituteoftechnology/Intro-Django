import graphene
from graphene_django import DjangoObjectType

from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User

    interfaces = (graphene.relay.Node, )

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    ok = graphene.Boolean()
    status = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=False)

    def mutate(self,info, username, email, password):

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        return CreateUser(user=user, ok=True, status='Success')


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

# ...code
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        print(User.username)
        return User.objects.all()