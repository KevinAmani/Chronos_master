#-*-coding=utf-8-*-
from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	message=models.CharField(max_length=300)
	
class Team(models.Model):
	'''
		姓名（name）
		性别（sex）
		出生年月日（birth）
		属性（tag）
		简介（abstract）
		头像（img地址）
	'''
	name=models.CharField(max_length=20)
	sex=models.CharField(max_length=5)
	birth=models.CharField(max_length=10)
	tag=models.CharField(max_length=200)
	abstract=models.CharField(max_length=200)
	img=models.CharField(max_length=100)
	
class Schedule(models.Model):
	name=models.CharField(max_length=50)
	stuff=models.CharField(max_length=100)
	during=models.CharField(max_length=50)
	deadline=models.CharField(max_length=50)
	
class The_System(models.Model):
	version=models.CharField(max_length=10)
	number_p=models.CharField(max_length=10)
	