import datetime
from django.db import models
from ...accounts.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.datetime.now())
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now())
    upload_date = models.DateTimeField(blank=True, null=True)
    owners = models.ManyToManyField(User, blank=True, null=False, default='')

    def __str__(self):
        return self.name
