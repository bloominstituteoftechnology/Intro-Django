from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import NotNote, TaskList

class NotNoteType(DjangoObjectType):

    class Meta:
        model = NotNote

        interfaces = (graphene.relay.Node,)

class TaskListType(DjangoObjectType):

    class Meta:
        model = TaskList

        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):

    notNotes = graphene.List(NotNoteType)
    tasklist = graphene.List(TaskListType)

    def resolve_tasklist(self, info):
        return TaskList.objects.all()

    def resolve_notNotes(self, info):
        return NotNote.objects.all()

schema = graphene.Schema(query=Query)