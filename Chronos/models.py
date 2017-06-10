#-*-coding=utf-8-*-
from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
	name=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	message=models.CharField(max_length=300)