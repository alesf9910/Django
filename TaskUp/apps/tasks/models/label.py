from django.db import models
from .basecolor import BaseColor
from .project import Project

class Label(BaseColor):
    name = models.CharField(max_length=100, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
