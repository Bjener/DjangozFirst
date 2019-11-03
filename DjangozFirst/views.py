from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return HttpResponse("首页")

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(username,pwd)
        if username == 'admin' and pwd == 'admin':
            return  HttpResponseRedirect('/show_index')
    return render(request,'login.html')

def register(request):
    print("request",request)
    if request.method == "POST":
        print(1111111)
        username = request.POST.get('name','admin')
        pwd = request.POST.get('password')
        return HttpResponseRedirect('/login')
    return  render(request,'register.html')

def show_index(request):
    num1 = 1
    str1 = 1
    tuple1 = (1,2)
    list = [ ]
    dict1 = {"name":"zhangsan"}
    set1 = {1,2,3}

    return  render(request,'index.html',locals())