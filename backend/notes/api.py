from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers, viewsets
from .models import PersonalNote, Note
import requests

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note
        
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.none()
 
    def get_queryset(self):
        user = self.request.user
        print(self.request.user)
        if user.is_anonymous: 
            return Note.objects.all()
        elif user:
             return PersonalNote.objects.filter(user=user)()
        else:
            return Note.objects.none()   
