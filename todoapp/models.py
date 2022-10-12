from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=25)
    details=models.TextField(max_length=750)
    priority=models.CharField(max_length=500)
    date=models.DateField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name