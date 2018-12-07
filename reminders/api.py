from rest_framework import serializers, viewsets
from .models import PersonalReminder, Reminder

class PersonalReminderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalReminder
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        reminder = PersonalReminder.objects.create(user=user, **validated_data)
        return reminder

class PersonalReminderViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalReminderSerializer
    queryset = PersonalReminder.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalReminder.objects.none()
        
        else:
            return PersonalReminder.objects.filter(user=user)



#// ******************


class ReminderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reminder
        fields = ('title', 'content')


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()