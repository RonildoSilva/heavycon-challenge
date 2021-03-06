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
from django.urls import path, re_path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from report import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('reports/', views.reportList.as_view()),
    path('report/<int:id>',views.reportList.as_view(), name='get_report_by_id'),
    
    # delete event
    #path('reports/<int:pk>',views.reportList.as_view()),

    path('reportresponses/', views.reportResponseList.as_view(), name='reponses'),

    path('users/', views.userList.as_view()),
    path('user/<int:id>',views.userList.as_view(), name='get_user_by_id'),
]