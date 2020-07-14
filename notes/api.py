from rest_framework import serializers, viewsets
from .models import PersonalPost

class PersonalPostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalPost
        fields = ('username','user_profile_img', 'post_img', 'likes')
    
    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalPost.objects.create(user = user, **validated_data)
        return note

class PersonalPostViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalPostSerializer
    queryset = PersonalPost.objects.none()   

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalPost.objects.none()
        else:
            return PersonalPost.objects.filter(user=user)