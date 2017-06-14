# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators import csrf
from Chronos.models import Message
import smtplib
from email.mime.text import MIMEText
import json
 
# 接收POST请求数据
def the_message(request):
	context={}
	rcontext={}
	if request.POST:
		try:
			context['name'] = request.POST['name']
			context['email']=request.POST['email']
			context['message']=request.POST['message']
			Themessage=Message(name=context['name'],email=context['email'],message=context['message'])
			Themessage.save()
			rcontext["message"]="Success"
			rcontext["code"]="1"
			rcontext["model"]="POST"
		except:
			rcontext["message"]="Failure can not find element in POST"
			rcontext["code"]="0"
			rcontext["model"]="POST"
	elif request.GET:
		try:
			context['name'] = request.GET['name']
			context['email']=request.GET['email']
			context['message']=request.GET['message']
			Themessage=Message(name=context['name'],email=context['email'],message=context['message'])
			Themessage.save()
			rcontext["message"]="Success"
			rcontext["code"]="1"
			rcontext["model"]="GET"
		except:
			rcontext["message"]="Failure can not find element in GET"
			rcontext["code"]="0"
			rcontext["model"]="GET"
	else:
		rcontext["message"]="Nothing in request"
		rcontext["code"]="0"
		rcontext["model"]="NONE"
	
	try:
		send_mail(context)
	except:
		rcontext["message"]="Success"
		rcontext["code"]="2"
		rcontext["model"]="Emil Failure"
	return HttpResponse(json.dumps(rcontext))
	
def send_mail(content):
	context="Contment by"+content['name']+'\n'+'Emil:'+content['email']+'\n'+'Contment:'+content['message']
	sub="The Contment from website"
	mailto_list=['318272797@qq.com']
	#,'376528106@qq.com']
	mail_host="smtp.163.com"
	mail_user="15861800534"
	mail_pass="19950314"
	mail_postfix="163.com"
	me="<"+mail_user+"@"+mail_postfix+">"
	msg=MIMEText(context,_subtype='plain')
	msg['Subject']=sub
	msg['From']=me
	msg['To']=";".join(mailto_list)
	
	try:
		server = smtplib.SMTP()
		server.connect(mail_host)                            #连接服务器
		server.login(mail_user,mail_pass)               #登录操作
		server.sendmail(me,mailto_list, msg.as_string())
		server.close()
		return True
	except Exception, e:
		return False
	
	