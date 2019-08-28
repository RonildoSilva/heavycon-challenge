from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    message=models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    supervisors = models.ManyToManyField(User, related_name='supervisors')

    def __str__(self):
        return self.message