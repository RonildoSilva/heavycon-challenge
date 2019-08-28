from django.db import models
from django.contrib.auth.models import User

from report.models import Report

class ReportResponse(models.Model):
    message = models.CharField(max_length=255)
    report  = models.ForeignKey(Report, on_delete=models.CASCADE, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.message
