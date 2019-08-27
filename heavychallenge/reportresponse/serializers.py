from rest_framework import serializers
from . models import ReportResponse

class reportResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportResponse
        fields = '__all__'