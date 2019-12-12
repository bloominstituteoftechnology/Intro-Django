from rest_framework import serializers, viewsets
from .models import StudentReport, Student, ProjectManager

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ('id', 'name', 'current_section')