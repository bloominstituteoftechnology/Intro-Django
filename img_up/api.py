from rest_framework import serializers, viewsets
from .models import Epilepsy, EpilepsyUserInput

class EpilepsySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EpilepsyUserInput
        fields = ('created_at', 'updated_at','numOfTotalCases','admin_name',
                  'state','numOfTotalCases','numOfChildCases','numOfAdultCases')

        def create(self, validated_data):
            user = self.context['request'].user
            data = EpilepsyUserInput.objects.create(user=user, **validated_data)
            return data



class EpilepsyViewSet(viewsets.ModelViewSet):
    serializer_class = EpilepsySerializer
    queryset = EpilepsyUserInput.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return EpilepsyUserInput.objects.none()
        else:
            return EpilepsyUserInput.objects.filter(user=user)