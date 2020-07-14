from rest_framework import serializers, viewsets
from .models import Task, PersonalTask

class PersonalTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalTask
        fields = ('name', 'description', 'isComplete')

    def create(self, validated_data):
        # import pdb; pbd.set_trace()
        user = self.context['request'].user
        task = PersonalTask.objects.create(user=user, **validated_data)
        return task

class PersonalTaskViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalTaskSerializer
    queryset = PersonalTask.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalTask.objects.none()
        else:
            return PersonalTask.objects.filter(user=user)