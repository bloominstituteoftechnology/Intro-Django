from rest_framework import serializers,viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalNote
        fields = '__all__'

class PersonalNoteViewSet(viewsets.ModelViewSet):

    queryset = PersonalNote.objects.all()
    serializer_class = PersonalNoteSerializer