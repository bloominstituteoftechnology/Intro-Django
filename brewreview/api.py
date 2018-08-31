from rest_framework import serializers, viewsets
from .models import Brew, Beans, Equitment


class BrewSerializer(serializers.HyperlinkedModelSerializer):
    beans_used = serializers.HyperlinkedIdentityField(
        view_name='BeansViewSet',
        lookup_field='beans_used',
        read_only=True
    )
    equitment_used = serializers.HyperlinkedRelatedField(
        view_name='EquitmentViewSet',
        lookup_field='equitment_used',
        many=True,
        read_only=True
    )

    class Meta:
        model = Brew
        fields = ('brew_id', 'beans_used', 'equitment_used', 'mass_beans', 'mass_water', 'brew_time', 'comments')

    def create(self, validated_data):
        # import pdb; pdb.set_trace
        user = self.context['request'].user
        brew = Brew.objects.create(user=user, **validated_data)
        return brew


class BrewViewSet(viewsets.ModelViewSet):
    serializer_class = BrewSerializer
    queryset = Brew.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Brew.objects.none()
        else:
            return Brew.objects.filter(user=user)




class BeansViewSet(viewsets.ModelViewSet):
    queryset = Beans.objects.all()


class EquitmentViewSet(viewsets.ModelViewSet):
    queryset = Equitment.objects.all()