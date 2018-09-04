import notes.schema
import video_archive.schema
import graphene

from graphene_django.debug import DjangoDebug


class SuperQuery(notes.schema.Query, video_archive.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


schema = graphene.Schema(query=SuperQuery)
