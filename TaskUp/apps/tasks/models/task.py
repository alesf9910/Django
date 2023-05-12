from datetime import datetime
from django.db import models
from .label import Label
from .project import Project
from .worker import Worker


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now())
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField(default=datetime.now())
    upload_date = models.DateTimeField(blank=True, null=True)
    labels = models.ManyToManyField(Label, blank=True)
    workers = models.ManyToManyField(Worker, through='WorkerTask')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
