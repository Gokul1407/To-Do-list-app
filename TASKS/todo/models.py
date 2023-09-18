from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=100)
    prio=models.CharField(max_length=100)
    date=models.DateField(null=True, blank=True)
    
    
    
   
