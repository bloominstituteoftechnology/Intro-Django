from django.db import models
from uuid import uuid4

# Create your models here.

class Section(models.Model):
  section_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  section_name = models.CharField(unique=True, max_length=10)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  class Meta:
      ordering = ('section_name',)

  def __str__(self):
    return self.section_name

class Student(models.Model):
  student_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  student_name = models.CharField(max_length=30)

  # Relationship Fields
  current_section = models.ForeignKey(Section,on_delete=models.CASCADE)
  # current_section = models.CharField(max_length=10)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
    
  def __str__(self):
    return self.student_name

class ProjectManager(models.Model):
  project_manager_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  project_manager_name = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.project_manager_name

class StudentReport(models.Model):
  student_report_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
  project_manager_id = models.ForeignKey(ProjectManager, on_delete=models.CASCADE)
  submitted_sprints = models.PositiveSmallIntegerField()
  passed_sprints = models.PositiveSmallIntegerField()
  sprint_pass_rate = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class SprintStatus(models.Model):

  class Meta:
    verbose_name_plural = "Sprint Status"

  sprint_status_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  sprint_status = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.sprint_status

class Sprint(models.Model):
  sprint_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  student_report_id = models.ForeignKey(StudentReport, on_delete=models.CASCADE)
  sprint_name = models.CharField(max_length=40)
  sprint_status_id = models.ForeignKey(SprintStatus, on_delete=models.CASCADE)
  submission_self_rating = models.PositiveSmallIntegerField()
  what_went_well = models.TextField(blank=True)
  what_could_have_gone_better = models.TextField(blank=True)
  review_rating = models.PositiveSmallIntegerField()
  review_great = models.TextField(blank=True)
  requested_improvements = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.sprint_name