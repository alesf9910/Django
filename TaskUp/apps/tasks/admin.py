from django.contrib import admin
from .models.basecolor import BaseColor
from .models.comment import Comment
from .models.label import Label
from .models.prettykeyword import PrettyKeyWord
from .models.project import Project
from .models.task import Task
from .models.worker import Worker
from .models.workertask import WorkerTask

# Register your models here.
admin.site.register(Label)
admin.site.register(PrettyKeyWord)
admin.site.register(Worker)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(WorkerTask)
admin.site.register(Comment)