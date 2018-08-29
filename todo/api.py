from rest_framework import serializers, viewsets
from .models import PersonalTodo

class PersonalTodoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PersonalTodo
        fields = ('title', 'description', 'isDone')


class PersonalTodoViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalTodoSerializer
    queryset = PersonalTodo.objects.all()