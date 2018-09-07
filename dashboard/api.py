# Day 3:
from rest_framework import serializers, viewsets
from .models import StudentReport, Student, ProjectManager
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
  serializer_class = StudentSerializer
  queryset = Student.objects.none()
  
  def get_queryset(self):
    user = self.request.user

    if user.is_anonymous:
      return Student.objects.none()
    else:
      return Student.objects.filter(user=user)
      # return Student.objects.all()


class StudentReportSerializer(serializers.ModelSerializer):
  student = StudentSerializer(many=False)

  # Inner class nested inside StudentReportSerializer
  class Meta:
    model = StudentReport
    fields = ('student', 'project_manager_id', 'submitted_sprints', 'passed_sprints')
    # fields = '__all__'

class StudentReportViewSet(viewsets.ModelViewSet):
  serializer_class = StudentReportSerializer
  queryset = StudentReport.objects.none()
  
  def get_queryset(self):
    user = self.request.user

    if user.is_anonymous:
      return StudentReport.objects.none()
    else:
      # return StudentReport.objects.filter(user=user)
      return StudentReport.objects.all()

