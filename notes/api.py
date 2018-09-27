from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model= PersonalNote
        fields= ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace() #start debugger here
        user=self.context[r'request'].user
        note=PersonalNote.objects.create(user=user, **validated_data) #**== key word argument
        return note


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class= PersonalNoteSerializer
    queryset= PersonalNote.objects.none()

    def get_queryset(self):
        user=self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)