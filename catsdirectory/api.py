from rest_framework import serializers, viewsets
from .models import PersonalCat

class PersonalCatSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalCat
        fields = ('breed', 'facts')
    

    def create(self, validated_data):
        #import pdb; pdb.set_trace()
        user = self.context['request'].user
        cat = PersonalCat.objects.create(user=user, **validated_data)
        return cat

class PersonalCatViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalCatSerializer
    queryset = PersonalCat.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalCat.objects.none()
            
        else:
            return PersonalCat.objects.filter(user=user)