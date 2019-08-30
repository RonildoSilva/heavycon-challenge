from rest_framework import serializers
from . models import Report
from . models import ReportResponse
from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):    

    class Meta:
        model = User
        fields = ('id','username')
        #fields = '__all__'

class reportResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportResponse
        fields = '__all__'

class reportSerializer(serializers.ModelSerializer):

    supervisors = userSerializer(read_only=True, many=True)

    class Meta:
        model = Report
        fields = ('message', 'author', 'supervisors')
        #fields = '__all__'
    
    def create(self, validated_data):
        supervisors_data = validated_data.pop('supervisors')
        report = Report.objects.create(**validated_data)
        for supervisor_data in supervisors_data:
            User.objects.create(report=report, **supervisor_data)
        
        return report