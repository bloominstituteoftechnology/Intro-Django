from rest_framework import serializers
from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'area')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

        
        #import pdb; pdb.set_trace()  # Start the debugger here
        

        # self.context[‘request’].user

    # def create(self, validated_data):
    #     user = self.context[‘request’].user
    #     note = PersonalNote.objects.create(user=user, **validated_data)
    #     return note

    # Inner class nested inside PersonalNoteSerializer


class PersonalNoteViewSet(viewsets.ModelViewSet):
        serializer_class = PersonalNoteSerializer
        queryset = PersonalNote.objects.all()