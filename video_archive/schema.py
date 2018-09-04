# from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalVideo as PersonalVideoModel


class PersonalVideo(DjangoObjectType):
    """Describe notes model you want to expose through GraphQL"""

    class Meta:
        model = PersonalVideoModel

        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    """Describe the records you want to show"""

    personalvideos = graphene.List(PersonalVideo)

    def resolve_personalvideos(self, info):
        """Decide what videos to return."""
        user = info.context.user

        if user.is_anonymous:
            return PersonalVideoModel.objects.none()
        else:
            return PersonalVideoModel.objects.filter(user=user)


class CreatePersonalVideo(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        link = graphene.String()

    personalvideo = graphene.Field(PersonalVideo)
    ok = graphene.Boolean()
    status = graphene.String()

    def mutate(self, info, title, link):
        user = info.context.user

        if user.is_anonymous:
            return CreatePersonalVideo(ok=False, status="Must be logged in!")
        else:
            new_video = PersonalVideoModel(title=title, link=link, user=user)
            new_video.save()
            return CreatePersonalVideo(personalvideo=new_video, ok=True, status="ok")


class VideoMutation(graphene.AbstractType):
    create_personal_video = CreatePersonalVideo.Field()
