from django.db import models

from datetime import datetime

# Create your models here.

class WorksPackage(models.Model):
    date = models.DateTimeField("date")


class Work(models.Model):
    name = models.CharField("name",max_length=200)
    start = models.DateTimeField("start")
    end = models.DateTimeField("end",null=True, blank=True)
    work = models.ForeignKey(WorksPackage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name