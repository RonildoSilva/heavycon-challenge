from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from . models import Report
from . models import ReportResponse

from . serializers import reportSerializer
from . serializers import reportResponseSerializer
from . serializers import userSerializer

class reportList(APIView):
    
    # return all data
    def get(self, request):
        report = Report.objects.all()
        serializer = reportSerializer(report, many=True)
        return Response(serializer.data)

    # return by id
    """    
    def get(self, request, pk):
        report = Report.objects.get(pk=pk)
        serializer = reportSerializer(report)
        return Response(serializer.data)
    """        

    def post(self, request):
        serializer = reportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = Report.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class reportResponseList(APIView):

    # return all data
    def get(self, request):
        report = ReportResponse.objects.all()
        serializer = reportResponseSerializer(report, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = reportResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userList(APIView):

    # return all data
    def get(self, request):
        users = User.objects.all()
        serializer = userSerializer(users, many=True)
        return Response(serializer.data)