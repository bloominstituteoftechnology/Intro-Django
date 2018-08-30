from rest_framework import serializers, viewsets
from .models import PrivateRecord


class PrivateRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrivateRecord
        fields = ('patient_name', 'DOB')
    
    def create(self, validated_data):
        user = self.context['request'].user
        record = PrivateRecord.objects.create(user=user, **validated_data)
        return record


class PrivateRecordViewSet(viewsets.ModelViewSet):
    serializer_class = PrivateRecordSerializer
    queryset = PrivateRecord.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PrivateRecord.objects.none()
        else:
            return PrivateRecord.objects.filter(user=user)