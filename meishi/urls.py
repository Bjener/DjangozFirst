from django.urls import path,include
from . import  views

urlpatterns = [
path('Text', views.Text),
path('index', views.index,name='index'),
path('pinpai/',views.pinpai,name='pinpai'),
path('meishi/',views.meishi,name='meishi'),
path('shop/',views.shop,name='shop'),
path('news/',views.news,name='news'),
path('about_us/',views.about_us,name="about_us"),

]
app_name='meishi'