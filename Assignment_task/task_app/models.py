from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    status = models.CharField(max_length=2,choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

