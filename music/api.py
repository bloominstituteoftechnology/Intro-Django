from rest_framework import serializers, viewsets
from .models import PersonalMusic

class PersonalMusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalMusic
        fields = ('title', 'composer_last_name', 'composer_first_name', 'publisher', 'notes')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalMusic.objects.create(user=user, **validated_data)
        return note
        
class PersonalMusicViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalMusicSerializer
    queryset = PersonalMusic.objects.all()