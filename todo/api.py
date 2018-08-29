from rest_framework import serializers, viewsets
from .models import PersonalTodo

class PersonalTodoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalTodo
        fields = ('title', 'description', 'isDone')

    def create(self, validated_data):
        user = self.context['request'].user
        todo = PersonalTodo.objects.create(user=user, **validated_data)
        return todo


class PersonalTodoViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalTodoSerializer
    queryset = PersonalTodo.objects.all()