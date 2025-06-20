from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(default='Description')
    until_time = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField('Done')
    pending = models.BooleanField('Pending')
    
    def __str__(self):
        return self.name