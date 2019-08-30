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

from django.core.exceptions import ObjectDoesNotExist

class reportList(APIView):

    def get(self, request, id=None):
        report = Report.objects.filter(author = id)
        serializer = reportSerializer(report, many=True)
        return Response(serializer.data)

    # return by id / all
    """
    def get(self, request, id=None):
        try:
            report = Report.objects.get(pk=id)
            serializer = reportSerializer(report)
            return Response(serializer.data)
        except:
            report = Report.objects.all()
            serializer = reportSerializer(report, many=True)
            return Response(serializer.data)
    """     

    def post(self, request):
        serializer = reportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        event = Report.objects.get(pk=id)
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
    def get(self, request, id=None):
        try:
            user = User.objects.get(pk=id)
            serializer = userSerializer(user)
            return Response(serializer.data)
        except:
            users = User.objects.all()
            serializer = userSerializer(users, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        