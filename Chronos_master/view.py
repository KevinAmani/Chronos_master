#-*-coding=utf-8-*-
from django.http import HttpResponse
from django.http import HttpRequest
from Chronos.models import Team,Schedule,The_System
import time

import json
 
def Team_data(request):#获取团队信息
	start=time.clock()
	response=list()
	rcontext={}
	try:
		the_list=Team.objects.all()
	except:
		rcontext['message']="Get data failure."
		rcontext['code']="0"
		rcontext['model']="None"
		return HttpResponse(json.dumps(rcontext))
	try:
		for var in the_list:
			member={}
			member['id']=var.id
			member['name']=var.name
			member['sex']=var.sex
			member['birth']=var.birth
			member['tag']=json.loads(var.tag)
			member['abstract']=var.abstract
			member['img']=var.img
			response.append(member)
	except:
		rcontext['message']="No Key in data."
		rcontext['code']="0"
		rcontext['model']="None"
		return HttpResponse(json.dumps(rcontext))
		
	rcontext['message']="Success."
	rcontext['code']="1"
	rcontext['model']=response
	end=time.clock()
	rcontext['time']=end-start
	
	return HttpResponse(json.dumps(rcontext))
	
def Schedule_data(request):#工作室更新计划
	start=time.clock()
	response=list()
	rcontext={}
	try:
		the_list=Schedule.objects.all()
	except:
		rcontext['message']="Get data failure."
		rcontext['code']="0"
		rcontext['model']="None"
		return HttpResponse(json.dumps(rcontext))
	try:
		for var in the_list:
			item={}
			item['id']=var.id
			item['name']=var.name
			item['stuff']=var.stuff
			item['during']=var.during
			item['deadline']=var.deadline
			response.append(item)
	except:
		rcontext['message']="No Key in data."
		rcontext['code']="0"
		rcontext['model']="None"
		return HttpResponse(json.dumps(rcontext))
		
	rcontext['message']="Success."
	rcontext['code']="1"
	rcontext['model']=response
	end=time.clock()
	rcontext['time']=end-start
	
	return HttpResponse(json.dumps(rcontext))
	
 
	