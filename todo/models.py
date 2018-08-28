from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    isDone = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.title}>'

class PersonalTodo(Todo):
    user = models.ForeignKey(User, on_delete=models.CASCADE)