from django.db import models
from .task import Task
from .worker import Worker

class WorkerTask(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.worker} - {self.task.name}"