from rest_framework import serializers, viewsets
from .models import PersonalNotNote, TaskList

class PerNotNoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        notNote = PersonalNotNote.objects.create(user=user,**validated_data)
        return notNote

    class Meta:
        model = PersonalNotNote
        fields = ('title', 'subtitle', 'content', 'extraContent')


class PerNotNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PerNotNoteSerializer
    queryset = PersonalNotNote.objects.none()

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        #THIS IS A DEBUGGER TOOL ^^

        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return PersonalNotNote.objects.none()
        else:
            return PersonalNotNote.objects.filter(user=logged_in_user)

class TaskListSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        tasks = TaskList.objects.create(user=user,**validated_data)
        return tasks

    class Meta:
        model = TaskList
        fields = ('task', 'description', 'due_date', 'completed')

class TaskListViewSet(viewsets.ModelViewSet):
    serializer_class = TaskListSerializer
    queryset = TaskList.objects.none()

    def get_queryset(self):
        logged_in_user = self.request.user

        if logged_in_user.is_anonymous:
            return TaskList.objects.none()
        else:
            return TaskList.objects.filter(user=logged_in_user)