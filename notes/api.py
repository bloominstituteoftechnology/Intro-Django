from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):   # inherit from the specific serializer we are using for this project

    class Meta: # Inner class nested inside PersonalNoteSerializer
        model = PersonalNote    # model
        fields = ('title', 'content')   # columns

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer   # rows
    queryset = PersonalNote.objects.all()   