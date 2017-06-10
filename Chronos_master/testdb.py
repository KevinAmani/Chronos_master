#-*-coding=utf-8-*-
from django.http import HttpResponse
 
from Chronos.models import Message
 
# 数据库操作
def testdb(request):
    test1=Message(name='xdf')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")