from rest_framework import serializers, viewsets
from .models import UserPost

class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    # Inner class nested inside UserPostSerializer
    class Meta:
        model = UserPost
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace() #starts the debugger here
        # run the server and then look in terminal
        # check out self.context['request'] in the debugger
        user = self.context['request'].user
        post = UserPost.objects.create(user = user, **validated_data)
        return post

class UserPostViewSet(viewsets.ModelViewSet):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return UserPost.objects.none()

        else:
            return UserPost.objects.filter(user = user)

