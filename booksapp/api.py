from rest_framework import serializers, viewsets
from .models import PersonalBook

class PersonalBookSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalBook
        fields = ('title', 'author')

    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user
        book = PersonalBook.objects.create(user=user,**validated_data)
        return book

class PersonalBookViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBookSerializer
    queryset = PersonalBook.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalBook.objects.none()
        else:
            return PersonalBook.objects.filter(user=user)
