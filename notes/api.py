from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ("title", "content")


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()


def create(self, validated_data):
    note = PersonalNote.objects.create(**validated_data)
    return note


def create(self, validated_data):
    import pdb

    pdb.set_trace()  # Start the debugger here
    pass


self.context[‘request’].user

def create(self, validated_data):
    user = self.context[‘request’].user
    note = PersonalNote.objects.create(user=user, **validated_data)
    return note

def get_queryset(self):
user = self.request.user

def get_queryset(self):
    user = self.request.user

    if user.is_anonymous:
        return PersonalNote.objects.none()
    else:
        return PersonalNote.objects.filter(user=user)

CORS_ORIGIN_ALLOW_ALL = True