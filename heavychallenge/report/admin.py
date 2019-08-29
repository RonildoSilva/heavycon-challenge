from django.contrib import admin
from . models import Report
from . models import ReportResponse

admin.site.register(Report)
admin.site.register(ReportResponse)