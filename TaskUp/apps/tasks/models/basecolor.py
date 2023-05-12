from django.db import models

class BaseColor(models.Model):
    color = models.CharField(max_length=9, blank=False, default="#ffffff")
    background_color = models.CharField(max_length=9, blank=False, default="#000000")

    class Meta:
        abstract = True
