from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    message=models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='', related_name='author')
    supervisors = models.ManyToManyField(User, related_name='supervisors')

    def __str__(self):
        return self.message


class ReportResponse(models.Model):
    message = models.CharField(max_length=255)
    report  = models.ForeignKey(Report, on_delete=models.CASCADE, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.message

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username        