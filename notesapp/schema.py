from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note, PersonalNote

class NoteType(DjangoObjectType):
  class Meta:
    model = Note
    interfaces = (graphene.relay.Node,)

class PersonalNoteType(DjangoObjectType):
  class Meta:
    model = PersonalNote
    interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
  notes = graphene.List(NoteType)
  personalnotes = graphene.List(PersonalNoteType)

  def resolve_notes(self, info):
    for note in Note.objects.all():
      print(note.title)
      print(note)
      #print(isinstance(note, type(Note)))
      #print('THIS', issubclass(type(note), Note))
      print('THIS', type(note) is PersonalNoteType)

    return Note.objects.all()

  def resolve_personalnotes(self, info):
    user = info.context.user
    if user.is_anonymous:
      return PersonalNote.objects.none()
    else:
      return PersonalNote.objects.filter(user=user)

schema = graphene.Schema(query=Query)
