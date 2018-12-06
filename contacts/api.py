from rest_framework import serializers, viewsets
from .models import Contact, PersonalContact


class PersonalContactSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalContact
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        contact = PersonalContact.objects.create(user=user, **validated_data)
        return contact


class PersonalContactViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalContactSerializer
    queryset = PersonalContact.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalContact.objects.none()
        else:
            return PersonalContact.objects.filter(user=user)
