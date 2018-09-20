from .models import Brewery, Beer, PersonalNote
import graphene
from graphene_django.fields import DjangoConnectionField, DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from django.conf import settings


class PersonalNoteNode(DjangoObjectType):
    class Meta:
        model = PersonalNote
        interfaces = (graphene.Node, )

class BreweryNode(DjangoObjectType):
    class Meta:
        model = Brewery
        interfaces = (graphene.Node, )

class BeerNode(DjangoObjectType):
    class Meta:
        model = Beer
        interfaces = (graphene.Node, )

class Query(graphene.ObjectType):

    personalnotes = DjangoFilterConnectionField(PersonalNoteNode, title=graphene.String())
    all_notes = DjangoConnectionField(PersonalNoteNode)

    breweries = graphene.List(BreweryNode)
    all_breweries = DjangoConnectionField(BreweryNode)

    beers = graphene.List(BeerNode)
    all_beers = DjangoConnectionField(BeerNode)

    def resolve_personalnotes(self, args, context, info):
        title = args.get('title')
        user = info.context.user
        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user, title=title)

    def resolve_brewery(self, info):
        return Brewery.objects.all()

    def resolve_beer(self, info):
        return Beer.objects.all()

class CreatePersonalNote(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content= graphene.String()

    personalnote = graphene.Field(PersonalNoteNode)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, content):
        user = info.context.user

        if user.is_anonymous:
            return CreatePersonalNote(ok=False, status="Must be logged in!")
        else:
            new_note = PersonalNote(title=title, content=content, user=user)
            new_note.save()
            return CreatePersonalNote(personalnote=new_note, ok=True, status="ok")

class CreateBrewery(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        address = graphene.String()
        website = graphene.String()

    brewery = graphene.Field(BreweryNode)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, name, address, website):
        new_brewery = Brewery(name=name, address=address, website=website)
        new_brewery.save()
        return CreateBrewery(brewery=new_brewery, ok=True, status="ok")

class Mutation(graphene.ObjectType):
    create_personal_note = CreatePersonalNote.Field()
    create_brewery = CreateBrewery.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)