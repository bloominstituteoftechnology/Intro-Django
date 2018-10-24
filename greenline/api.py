from rest_framework import serializers, viewsets
from .models import UserPost

class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    # Inner class nested inside UserPostSerializer
    class Meta:
        model = UserPost
        fields = ('title', 'content')

    def create(self, validated_data):
        import pdb; pdb.set_trace() #starts the debugger here
        post = UserPost.objects.create(**validated_data)
        return post

class UserPostViewSet(viewsets.ModelViewSet):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()

