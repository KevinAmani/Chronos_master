# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators import csrf
from Chronos.models import Message
import json
 
# 接收POST请求数据
def search_post(request):
	context={}
	rcontext={}
	if request.POST:
		try:
			context['name'] = request.POST['name']
			context['email']=request.POST['email']
			context['message']=request.POST['message']
			Themessage=Message(name=context['name'],email=context['email'],message=context['message'])
			Themessage.save()
			rcontext["message"]="success"
			rcontext["code"]="1"
			rcontext["model"]="POST"
		except:
			rcontext["message"]="failure can not find element in POST"
			rcontext["code"]="0"
			rcontext["model"]="POST"
	elif request.GET:
		try:
			context['name'] = request.GET['name']
			context['email']=request.GET['email']
			context['message']=request.GET['message']
			Themessage=Message(name=context['name'],email=context['email'],message=context['message'])
			Themessage.save()
			rcontext["message"]="success"
			rcontext["code"]="1"
			rcontext["model"]="GET"
		except:
			rcontext["message"]="failure can not find element in GET"
			rcontext["code"]="0"
			rcontext["model"]="GET"
	else:
		rcontext["message"]="failure"
		rcontext["code"]="0"
		rcontext["model"]="NONE"
	#return HttpResponse(json.dumps(rcontext))
	#return HttpResponse(json.dumps(request.body))
	return render(request,"post.html",context)
	
	
	
def search_message(request):
	context={}
	rcontext={}
	if request.POST:
		try:
			context['name'] = request.POST['name']
			context['email']=request.POST['email']
			context['message']=request.POST['message']
			Themessage=Message(name=context['name'],email=context['email'],message=context['message'])
			Themessage.save()
			rcontext["message"]="success"
			rcontext["code"]="1"
			rcontext["model"]="POST"
		except:
			rcontext["message"]="failure can not find element in POST"
			rcontext["code"]="0"
			rcontext["model"]="POST"
	elif request.GET:
		try:
			context['name'] = request.GET['name']
			context['email']=request.GET['email']
			context['message']=request.GET['message']
			Themessage=Message(name=context['name'],email=context['email'],message=context['message'])
			Themessage.save()
			rcontext["message"]="success"
			rcontext["code"]="1"
			rcontext["model"]="GET"
		except:
			rcontext["message"]="failure can not find element in GET"
			rcontext["code"]="0"
			rcontext["model"]="GET"
	else:
		request=json.loads(request.POST)
		try:
			context['name'] = request['name']
			context['email']=request['email']
			context['message']=request['message']
			Themessage=Message(name=context['name'],email=context['email'],message=context['message'])
			Themessage.save()
			rcontext["message"]="success"
			rcontext["code"]="1"
			rcontext["model"]="JSON"
		except:
			rcontext["message"]=request
			rcontext["code"]="0"
			rcontext["model"]="POST"
		#return HttpResponse(json.dumps(rcontext))
		#return HttpResponse(json.dumps(request.body))
	return render(request,"post.html",context)