from django.db import models
from uuid import uuid4

# Create your models here.
class StudentReport(models.Model):
  student_report_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  student_name = models.CharField(max_length=30)
  current_section = models.CharField(max_length=10)
  project_manager = models.CharField(max_length=30)
  submitted_sprints = models.PositiveSmallIntegerField()
  passed_sprints = models.PositiveSmallIntegerField()
  sprint_pass_rate = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class Sprint(models.Model):
  sprint_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  student_report_id = models.ForeignKey(StudentReport, on_delete=models.CASCADE)
  sprint_name = models.CharField(max_length=40)
  sprint_status = models.CharField(max_length=20)
  submission_self_rating = models.PositiveSmallIntegerField()
  what_went_well = models.TextField(blank=True)
  what_could_have_gone_better = models.TextField(blank=True)
  review_rating = models.PositiveSmallIntegerField()
  review_great = models.TextField(blank=True)
  requested_improvements = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)