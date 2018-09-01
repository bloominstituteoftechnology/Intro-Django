from rest_framework import serializers, viewsets
from .models import PersonalNote
# get the data out of the database and present it 

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer): # gives us nice hyperlink view of it when looking through a web browser
    
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    
    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user 
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note 

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user 

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)