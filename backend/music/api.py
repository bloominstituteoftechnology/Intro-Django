from rest_framework import serializers, viewsets
from .models import PersonalMusic, Music
from django.db import models

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ('title', 'composer_last_name', 'composer_first_name', 'publisher', 'notes')

    def create(self, validated_data):
        user = self.context['request'].user
        note = Music.objects.create(user=user, **validated_data)
        return note
        
class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Music.objects.all()
        elif not user:
            return Music.objects.all()

        else:
            return Music.objects.filter(user=user)
            