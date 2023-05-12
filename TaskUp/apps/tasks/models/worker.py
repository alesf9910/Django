from django.db import models

from .project import Project
from ...accounts.models import User

class Worker(models.Model):
    rol = models.CharField(max_length=150, blank=False, null=False, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} {self.rol}"
