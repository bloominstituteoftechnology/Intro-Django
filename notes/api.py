from rest_framework import serializers, viewsets
from .models import Author, Note, PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'body')

    def create(self, validated_data):
        current_user = self.context['request'].user
        
        # current_author = Author.object.filter(user = current_user)
        # returns query set
        current_author = Author.objects.get(user = current_user)
        # returns a single obj


        note = PersonalNote.objects.create( author=current_author, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        current_user = self.request.user
        # user not logged in 
        if current_user.is_anonymous:
            return PersonalNote.objects.none()
        #if admin
        elif current_user.is_superuser:
            return PersonalNote.objects.all()
        # user logged in
        else:
            current_user = self.request.user
            current_author = Author.objects.get(user=current_user)
            return PersonalNote.objects.filter(author=current_author)
