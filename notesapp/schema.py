from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote
from graphene_django import DjangoConnectionField


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
  # personalnotes = graphene.List(PersonalNoteType)

  # def resolve_personalnotes(self, info):
  #   user = info.context.user
  #   if user.is_anonymous:
  #     return PersonalNote.objects.none()
  #   else:
  #     return PersonalNote.objects.filter(user=user)

schema = graphene.Schema(query=Query)
