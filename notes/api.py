from rest_framework import serializers
from .models import Author, Note, PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
