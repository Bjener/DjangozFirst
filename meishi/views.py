from django.shortcuts import render
from.admin import Type

# Create your views here.
def Text(request):
    return render(request, 'Base/Text.html')

def index(request):
    return render(request, 'changed/index.html')

def pinpai(request):
    return render(request, 'changed/pinpai.html')


def meishi(request):
    type_list = Type.objects.all() #查询该表中所有的数据
    # print(type_list,type(type_list))
    for t in type_list:
        print(t.name,t.id)
    return render(request,'new_html/meishi.html',{"type_list":type_list})

def shop(request):
    return render(request,'new_html/shop.html')

def news(request):
    return render(request,'new_html/news.html')

def about_us(request):
    return render(request,'new_html/about-us.html')
