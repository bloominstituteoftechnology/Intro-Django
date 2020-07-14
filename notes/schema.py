from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote

class PersonalNoteType(DjangoObjectType):
    
    class Meta:
        model = PersonalNote
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    notes = graphene.List(PersonalNoteType)

    def resolve_notes(self, info):
        user = info.context.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)

class CreatePersonalNote(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    personalnote = graphene.Field(PersonalNoteType)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, content):
        user = info.context.user
        
        if user.is_anonymous:
            return CreatePersonalNote(ok=False, status="must be logged in")
        else:
            new_note = PersonalNote(title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personalnote=new_note, ok=True, status="success")

class Mutation(graphene.ObjectType):
    create_personal_note = CreatePersonalNote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)