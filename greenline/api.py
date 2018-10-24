from rest_framework import serializers, viewsets
from .models import UserPost

class UserPostSerializer(serializers.HyperlinkedModelSerializer):

# Inner class nested inside UserPostSerializer
    class Meta:
        model = UserPost
        fields = ('title', 'content')

class UserPostViewSet(viewsets.ModelViewSet):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()

