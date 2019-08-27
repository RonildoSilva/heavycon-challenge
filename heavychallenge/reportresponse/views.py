from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import ReportResponse
from . serializers import reportResponseSerializer

class reportResponseList(APIView):

    # return all data
    def get(self, request):
        report = ReportResponse.objects.all()
        serializer = reportResponseSerializer(report, many=True)
        return Response(serializer.data)