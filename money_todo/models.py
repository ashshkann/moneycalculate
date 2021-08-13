from django.db import models
from django.db.models import base

# Create your models here.

class creat_todo_models(models.Model):
    todo_date = models.CharField(max_length=50)
    todo_start_time = models.TimeField(auto_now=False, auto_now_add=False)
    todo_end_time = models.TimeField(auto_now=False, auto_now_add=False)
    todo_all_time = models.CharField(max_length=50)
    todo_day = models.CharField(max_length=50)

    def __str__(self):
        return self.todo_date
