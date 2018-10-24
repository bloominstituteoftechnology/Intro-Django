from rest_framework import serializers, viewsets

from .models import PersonalWhiskey

class PersonalWhiskeySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalWhiskey
        fields = ('title', 'description', 'notes')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()  # Start the debugger here
        user = self.context['request'].user
        whiskey = PersonalWhiskey.objects.create(user=user, **validated_data)
        return whiskey

class PersonalWhiskeyViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalWhiskeySerializer
    queryset = PersonalWhiskey.objects.all()