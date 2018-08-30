from rest_framework import serializers, viewsets
from .models import Gifter, Wishlist

class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        user = self.context['request'].user
        gifter = Wishlist.objects.create(user=user, **validated_data)
        return gifter

    class Meta:
        model = Wishlist
        fields = ('username', 'birthday')

class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    queryset = Gifter.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Wishlist.objects.none()
        else:
            return Wishlist.objects.filter(user=user)