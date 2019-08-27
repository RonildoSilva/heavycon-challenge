"""heavychallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from report import views
from reportresponse import response_views

from report import views
from reportresponse import response_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports/', views.reportList.as_view()),
    
    # delete event
    #path('reports/<int:pk>',views.reportList.as_view()),

    path('reportresponses/', response_views.reportResponseList.as_view(), name='reponses')
]