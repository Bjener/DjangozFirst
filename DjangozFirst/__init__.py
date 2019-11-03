from django.shortcuts import render
from django.http import HttpResponse

def index(request):   #
    return HttpResponse("Hello world!")

def login(request):
    a = "<a href = 'https://www.baidu.com/'>百度"
    username = request.GET.get('username')
    pwd = request.GET.get('password')
    print(username,pwd)
    return render(request,'login.html',{"a":a})   #可以返回字符串或者返回html标签

def show_index(request):
    return render(request,'index.html',{'index':"首页"})