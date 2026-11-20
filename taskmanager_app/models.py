from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    PRIORITY_CHOICES=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ]
    priority_model=models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    due_date=models.DateField(null=True,blank=True)
    overdue=models.BooleanField(default=False)