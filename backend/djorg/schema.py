import graphene

import notes.schema
import users.schema


class Query(users.schema.Query, notes.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, notes.schema.Mutation, graphene.ObjectType,):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)