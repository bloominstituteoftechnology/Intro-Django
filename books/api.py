from rest_framework import serializers, viewsets
from .models import PersonalBook

class PersonalBookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalBook
        fields = ('title', 'genre')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        book = PersonalBook.objects.create(user=user, **validated_data)
        return book

class PersonalBookViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBookSerializer
    queryset = PersonalBook.objects.all()
