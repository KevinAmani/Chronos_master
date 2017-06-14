#-*-coding=utf-8-*-
"""Chronos_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
 
from . import view,testdb,message
 
urlpatterns = [
    #url(r'^$', view.hello),
	#url(r'^test',testdb.testdb),
	url(r'^message',message.the_message),
	url(r'^team',view.Team_data),
	url(r'^schedule',view.Schedule_data),
]