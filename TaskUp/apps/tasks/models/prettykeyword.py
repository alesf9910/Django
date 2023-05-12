from django.db import models

from .basecolor import BaseColor
from .task import Task

class PrettyKeyWord(BaseColor):
    content = models.TextField(blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"
