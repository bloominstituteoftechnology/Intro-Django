from rest_framework import serializers, viewsets
from .models import Question

class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date' )
    
    def create(self, validated_data):
        question = Question.objects.create(**validated_data)
        return question

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        return Question.objects.all()