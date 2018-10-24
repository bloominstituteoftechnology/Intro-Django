from rest_framework import serializers
from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        note = PersonalNote.objects.create(**validated_data)
        return note

    def create(self, validated_data):
        import pdb; pdb.set_trace()  # Start the debugger here
        pass

        # self.context[‘request’].user

    # def create(self, validated_data):
    #     user = self.context[‘request’].user
    #     note = PersonalNote.objects.create(user=user, **validated_data)
    #     return note

    # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()