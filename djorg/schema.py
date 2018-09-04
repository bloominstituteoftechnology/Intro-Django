import notes.schema
import video_archive.schema
from notes.schema import NotesMutation
from video_archive.schema import VideoMutation
import graphene

from graphene_django.debug import DjangoDebug


class SuperQuery(notes.schema.Query, video_archive.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


class Mutation(NotesMutation, VideoMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=SuperQuery, mutation=Mutation)
