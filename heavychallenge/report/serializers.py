from rest_framework import serializers
from . models import Report
from . models import ReportResponse
from django.contrib.auth.models import User

class reportResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportResponse
        fields = '__all__'

class reportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
