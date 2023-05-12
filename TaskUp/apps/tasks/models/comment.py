import datetime
from django.db import models
from .task import Task
from ...accounts.models import User


class Comment(models.Model):
    content = models.JSONField()
    created_date = models.DateTimeField(default=datetime.datetime.now())
    update_date = models.DateTimeField(default=datetime.datetime.now())
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task.name} - {self.content}"
