from rest_framework import serializers, viewsets
from epilepsy.models import EpilepsyData, PersonalEpilepsyData

class PersonalEpilepsyDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalEpilepsyData
        fields = ('state', 'numOfDiagnoses')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()  # Start the debugger here
        user = self.context['request'].user
        note = PersonalEpilepsyData.objects.create(user=user, **validated_data)
        return note

class PersonalEpilepsyDataViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalEpilepsyDataSerializer
    queryset = PersonalEpilepsyData.objects.none()
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalEpilepsyData.objects.none()
        else:
            return PersonalEpilepsyData.objects.filter(user=user)