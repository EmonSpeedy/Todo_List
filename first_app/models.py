from django.db import models

# Create your models here.

class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    is_completed = models.BooleanField(default=False)
