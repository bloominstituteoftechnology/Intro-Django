from rest_framework import serializers, viewsets
from .models import PersonalThing


class PersonalThingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalThing
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        thing = PersonalThing.objects.create(user=user, **validated_data)
        return thing


class PersonalThingViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalThingSerializer
    queryset = PersonalThing.objects.all()

    def get_queryset(self):
        # import pdb; pdb.set_trace()

        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return PersonalThing.objects.none()
        else:
            return PersonalThing.objects.filter(user=logged_in_user)
