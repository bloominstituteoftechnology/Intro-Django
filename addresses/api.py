from rest_framework import serializers, viewsets
from .models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = ('friend', 'address')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        address = Address.objects.create(user=user, **validated_data)
        return address


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Address.objects.none()

        else:
            return Address.objects.filter(user=user)
