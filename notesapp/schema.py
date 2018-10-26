from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note, PersonalNote
from graphene_django import DjangoConnectionField

class NoteType(DjangoObjectType):
  class Meta:
    model = Note
    interfaces = (graphene.relay.Node,)

class PersonalNoteType(DjangoObjectType):
  class Meta:
    model = PersonalNote
    interfaces = (graphene.relay.Node,)
    #filter_fields = ['title', 'content']
    filter_fields = {
      'title': ['exact', 'icontains', 'istartswith'],
      'content': ['exact', 'icontains'],
    }


class Query(graphene.ObjectType):
  personalnotes = DjangoConnectionField(PersonalNoteType)
  # notes = graphene.List(NoteType)
  # personalnotes = graphene.List(PersonalNoteType)


  # def resolve_notes(self, info):
  #   user = info.context.user
  #   print(user)
  #   for note in Note.objects.all():
  #     print('1', note == Note)
  #     print('INST', isinstance(note, PersonalNote))
  #     print('SUB', issubclass(type(note), Note))
  #     print('TYPE', type(note) is Note)
  #     print(type(note))
  #     print('OIOI', type(note) == Note)
  #     print(note.__class__)

  #   return Note.objects.all()


  # def resolve_personalnotes(self, info):
  #   user = info.context.user
  #   if user.is_anonymous:
  #     return PersonalNote.objects.none()
  #   else:
  #     return PersonalNote.objects.filter(user=user)


schema = graphene.Schema(query=Query)
